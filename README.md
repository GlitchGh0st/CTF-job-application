# CTF-job-application
I leveraged my Python-developed Capture The Flag (CTF) project as part of my application for a Junior Ethical Hacker position.

# README for XOR-Encrypted Link Revealer with Matrix Rain

## Overview

This script is a fun, interactive way to reveal a XOR-Base64 encrypted link, typically to a resource such as a Google Drive link. It engages the user with a riddle and a second question, and upon successful answering, reveals the encrypted link. If the answer is incorrect, the script displays a cool  'Matrix rain' effect in the terminal.

## Features

Riddle Challenge: A simple riddle to test the user. (you can change the riddle and also provide a new hashed awnser to it in the script)

Password Challenge: A simple question to test the user. (Please provide your own question and hashed awnser in the script)

XOR-Base64 Encrypted Link: Securely stores an encrypted link that is revealed upon correctly answering the second question. (use your own link)

Matrix Rain Effect: Displays a Matrix-style rain animation in the terminal as a response to incorrect answers.


## Setup and Configuration

Clone the Repository

git clone [repo-link]
cd [repo-name]

## Install Dependencies

Ensure Python is installed on your system.
No external libraries are required for this script.

## Configuration

![Don't forget to change this](https://github.com/GlitchGh0st/CTF-job-application/blob/main/Screenshot%202024-01-03%20160734.png)

IMPORTANT: You must replace the placeholder for the Base64 encoded link with an actual XOR-Base64 encoded link (e.g., to a Google Drive file). If this is not done, the script will not function correctly and may throw errors.
To encode your link in XOR-Base64, use a suitable encoder and replace the value in the base64_encrypted_link variable.
The riddle and its answer hash can be customized as per your requirement. I used an image of a white rabbit with custom EXIF data that provided a new link to my CV!


## Running the Script

Simply execute the script in a Python environment:

python [script-name].py


# Matrix Rain Effect

![Matrix Rain Effect](https://github.com/GlitchGh0st/CTF-job-application/blob/main/Screenshot%202024-01-03%20155642.png)


The Matrix rain effect is a visually striking feature that activates when a user inputs an incorrect answer to the riddle. It simulates the iconic green rain from 'The Matrix' movie series in the terminal window.


## Code Obfuscation for Enhanced Security

If you're concerned about the security and reverse engineering of the CTF (Capture The Flag) Python script, it's a good practice to obfuscate the code. Obfuscation makes the code harder to understand and reverse engineer, adding an extra layer of protection.

I recommend using PyObfuscate for this purpose. PyObfuscate is an online tool that can obfuscate your entire Python code easily and effectively.

## Steps to Obfuscate Your Code:

Visit PyObfuscate. ( https://pyobfuscate.com/pyd  )

Copy and paste your entire Python script into the provided text area.
Click on the obfuscate button to process your code.
Replace your original script with the obfuscated version in your repository.

Note: While obfuscation increases security against reverse engineering, it does not make the code invulnerable. It is still important to follow best practices for security in your code development.


## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## License

Distributed under the MIT License. See LICENSE for more information.

## Acknowledgements

This script is inspired by the classic Matrix digital rain and cryptography puzzles.
Thanks to all contributors who help in improving and maintaining this project.

