
import datetime
import subprocess
import sys
from urllib.parse import quote_plus
import webbrowser

import speech_recognition as sr


def speak(text: str, engine=None) -> None:
    """Speak a response using a separate Python process."""
    print(f"Assistant: {text}")

    speech_script = """
import sys
import pyttsx3

speaker = pyttsx3.init("sapi5")
speaker.setProperty("volume", 1.0)
speaker.setProperty("rate", 150)
speaker.say(sys.argv[1])
speaker.runAndWait()
speaker.stop()
"""

    try:
        result = subprocess.run(
            [sys.executable, "-c", speech_script, text],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )

        if result.returncode != 0:
            print("Speech process error:")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Speech playback timed out.")
    except OSError as error:
        print(f"Could not start speech process: {error}")


def listen(recognizer: sr.Recognizer) -> str:
    try:
        with sr.Microphone() as source:
            print("\nListening... Speak now.")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5,
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8,
            )

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You: {command}")

        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected. Please try again.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")

    except sr.RequestError:
        print(
            "Speech recognition failed. "
            "Please check your internet connection."
        )

    except OSError as error:
        print(f"Microphone error: {error}")

    return ""


def main() -> None:
    recognizer = sr.Recognizer()

    speak(
        "Hello! I am your AI voice assistant Jarvis. "
        "How can I help you?"
    )

    while True:
        command = listen(recognizer)
        if not command:
            continue

        if any(
            phrase in command
            for phrase in (
                "exit",
                "stop",
                "goodbye",
                "thank you",
            )
        ):
            speak("Goodbye! Have a nice day.")
            break

        elif "time" in command:
            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )
            speak(f"The current time is {current_time}.")

        elif "date" in command or "today" in command:
            current_date = datetime.datetime.now().strftime(
                "%B %d, %Y"
            )
            speak(f"Today's date is {current_date}.")

        elif "search" in command:
            query = command.replace("search", "", 1).strip()

            if query:
                speak(f"Searching the web for {query}.")

                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(query)
                )

                webbrowser.open(url)

            else:
                speak("Please tell me what you want to search for.")

        elif "hello" in command or "hi" in command:
            speak("Hello! How are you?")

        else:
            speak(
                "I can tell you the time or date, "
                "search the web, or say goodbye to exit."
            )

if __name__ == "__main__":
    main()
