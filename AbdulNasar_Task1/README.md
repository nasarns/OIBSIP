Voice Assistant (TASK 1):

Project Description:
   This is a Python-based voice assistant that listens to spoken commands and replies out loud. It can tell you the current date and time, and it can open Google searches based on what you say.

Features:
   =>Voice input: Captures and understands spoken commands using SpeechRecognition and PyAudio.
   =>Spoken responses:talks back to the user through pyttsx3 text-to-speech.
   =>Date and time:Announces the current date and time on request.
   =>Voice-activated search:Opens Google search results for whatever you ask it to look up in the internet


Technologies Used:
   =>Python 3.13
   =>SpeechRecognition
   =>PyAudio
   =>pyttsx3

Installation and Execution:
   1.Install Python 3.13 on your system.
   2.Install the required libraries by running:
      pip install SpeechRecognition PyAudio pyttsx3

   3.Start the assistant with:
      python voice_assistant.py
   
Example Commands:
   1.Hello
   2.What is the time?
   3.Tell me today's date
   4.Search Python tutorials
   5.Goodbye

   Project Structure:
   ---------------------
      AbdulNasar_Task1/
      │
      ├── voice_assistant.py
      ├── README.md
      ├── requirements.txt
      │
      ├── screenshots/
      │   ├── assistant_greeting.png
      │   ├── time_date_response.png
      │   └── web_search_demo.png
      │
      └── recordings/
         └── voice_assistant_demo.mp4

Learning Outcomes:
   Developing this voice assistant gave me hands-on experience building a speech-driven Python application. I used speech recognition to turn spoken commands into text and text-to-speech to reply aloud, while handling microphone input, date and time queries, and voice-triggered web searches. It also strengthened my skills in exception handling, library integration, and subprocess execution for more reliable speech playback.
   
Internship:
    Organization: OASIS INFOBYTE
    Track: Python Programming Internship
    Task: Task 1  Voice Assistant

Author:
    Abdul Nasar

