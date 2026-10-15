Random Password Generator (TASK 2):

Project Description:
    =>This project is a Python-based Random Password Generator developed as part of the OASIS INFOBYTE Python Programming Internship.
    =>The program helps users to create passwords by choosing the desired length and the character types they want to include. 
    =>It validates users input before generating a password and lets users to create another password without restarting the application.

Features:
    * Custom password length: Allows users to specify the password length, with a minimum of 8 characters.
    * Character selection: Supports uppercase letters, lowercase letters, digits, and symbols.
    * Input validation: Handles non-numeric lengths, short passwords, and invalid character-type selections.
    * Character-type requirements: Requires at least two different character types and includes every selected type in the generated password.
    * Password regeneration: Lets users generate additional passwords in the same session.
    * Secure random selection: Uses Python’s secrets module to select characters.

Technologies Used:
    * Python 3
    * secrets — random character selection
    * string — predefined character sets

The required modules are included in Python’s standard library, so no additional package installation is needed.

Project Structure:

    AbdulNasar_Task3/
    ├── password_generator.py
    ├── README.md
    └── screenshots/
        ├── password_generated.png
        ├── invalid_input.png
        ├── regenerate_password.png
        └── character_validation.png


How to Run the Project:

1.Check Python is installed:

    =>Make sure Python is installed. Check the version with:

    =>python --version

    
2.Open the project folder:

    =>Open the project folder in VS Code and open its terminal.

3.Run the program:

Execute:

    command: python password_generator.py
    

How to Use:

    1. Enter the required password length. The value must be at least 8.
    2. Select character types using the displayed options:
        * 1 -Uppercase letters
        * 2 -Lowercase letters
        * 3 -Numbers
        * 4 -Symbols
    3. Enter at least two different options, separated by commas. For example, 1,2,3,4.
    4. View the generated password.
    5. Enter y to generate another password or n to exit.

Testing:
 =>This program was tested for the following scenarios:
    -----------------------------    -------------------------------------------
        Test scenario	                        Expected behaviour
    -----------------------------    -------------------------------------------
    Valid password length	       -  Accepts the requested length
    Length below 8	               -  Requests a valid length
    Non-numeric length	           -  Displays an input error
    Only one character type	       -  Requests at least two types
    Invalid character-type option  -  Rejects the selection
    Multiple character types	   -  Includes every selected type
    Regeneration	               -  Generates another password
    Exit option                    -  Ends the program



Learning Outcomes:
   This project provided practical experience with Python functions, loops, conditional statements, exception handling, string operations, sets, and secure random selection. It also demonstrated how input validation can make a command-line application more reliable.

Internship:
    Organization: OASIS INFOBYTE
    Track: Python Programming Internship
    Task: Task 3  Random Password Generator

Author:
    Abdul Nasar