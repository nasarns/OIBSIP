
import secrets
import string

print("-" * 40)
print("     RANDOM PASSWORD GENERATOR")
print("-" * 40)

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password must contain at least 8 characters.")
        else:
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")


print("\nSelect the character types you want:")
print("1. Uppercase letters")
print("2. Lowercase letters")
print("3. Numbers")
print("4. Symbols")

while True:
    choices = input(
        "\nEnter your choices separated by commas (example: 1,2,3,4): "
    )

    selected = set(choices.replace(" ", "").split(","))

    if not selected.issubset({"1", "2", "3", "4"}):
        print("Invalid choice. Please select options from 1 to 4.")
        continue

    if len(selected) < 2:
        print("Please select at least two different character types.")
        continue

    break

characters = ""
required_characters = []

if "1" in selected:
    characters += string.ascii_uppercase
    required_characters.append(secrets.choice(string.ascii_uppercase))

if "2" in selected:
    characters += string.ascii_lowercase
    required_characters.append(secrets.choice(string.ascii_lowercase))

if "3" in selected:
    characters += string.digits
    required_characters.append(secrets.choice(string.digits))

if "4" in selected:
    characters += string.punctuation
    required_characters.append(secrets.choice(string.punctuation))


while True:
    password_characters = required_characters.copy()

    remaining_length = length - len(password_characters)

    for _ in range(remaining_length):
        password_characters.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_characters)

    password = "".join(password_characters)

    print("\nYour generated password is:")
    print(password)

    again = input("\nGenerate another password? (y/n): ").strip().lower()

    if again == "n":
        print("\nThank you for using the Password Generator!")
        break

    elif again != "y":
        print("Please enter y or n.")
