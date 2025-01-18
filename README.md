# Chatbot Auto-Responder

This project automates the process of reading chat messages from WhatsApp, processing them using OpenAI's GPT model, and sending back responses. It is built using Python and utilizes libraries like pyautogui for mouse and keyboard automation, pyperclip for clipboard management, and the openai API for natural language processing.

## Features

- Automates reading chat messages from WhatsApp.
- Retrieves the latest message and checks the sender.
- Sends the chat history to OpenAI's GPT model for processing.
- Pastes the generated response back into the chat.
- Executes the entire process using Python scripts with a simple click and drag to select the text.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - pyautogui
  - pyperclip
  - openai
  
## Setup

API Key: You need to have an OpenAI API key. Replace "API_KEY" with your actual OpenAI API key in the script.

Running the Script: Simply run the script in your Python environment. The automation will begin by clicking on the specified coordinates on your screen, selecting the WhatsApp chat text, and interacting with the chat window.

Customization: Modify the coordinates in the script based on your screen resolution or if you want to adjust the automation to a different window.

## How It Works

The script clicks on a specific location on the screen to focus the WhatsApp window.
It uses pyautogui to select the chat history and copies it to the clipboard.
The chat history is then processed using OpenAI's GPT model.
The script generates a response and copies it back to the clipboard.
Finally, it pastes the response into the chat and sends it by pressing Enter.

## How to Use

Clone or download the repository.
Open the script file and ensure you have set your OpenAI API key.
Run the script, and the automation will start.
The script will handle the process of reading and responding to WhatsApp messages automatically.

## Limitations

The script relies on screen coordinates, so it may not work on all screen resolutions or setups.
The automation process is sensitive to the position of the WhatsApp window on your screen.
It is designed for WhatsApp Web on a desktop, and may not work with other messaging platforms.
