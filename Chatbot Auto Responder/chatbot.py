
import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key = "API_KEY"
)


def is_last_message_from_sender(chat_log, sender_name = ".."):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    else:
        return False


# Step 1: Click on the icon at cooordinates(1212,1047)
pyautogui.click(1212,1047)
time.sleep(1)   # Wait for 1 second to ensure the click is registered

# Step 2: Drag the mouse from (498, 152) to (1857, 926) to select the text
pyautogui.moveTo(498, 152)
pyautogui.dragTo(1857, 926, duration=1.5, button ='left')  # Drag for 1 sec

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click(1501,897)

# Step 4: Retrieve text from clipboard and store it
chatHistory = pyperclip.paste()

# Print copied text
print(chatHistory)
print(is_last_message_from_sender(chatHistory))

if is_last_message_from_sender(chatHistory):    
    completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "......"},
        {"role": "user", "content": chatHistory}
    ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)

# Step 5: Click at coordinates (1808, 1328)
time.sleep(1) # Wait a sec to ensure click is generated

# Step 6: Paste the text
pyautogui.hotkey('ctrl', 'v')
time.sleep(1) # Wait for a sec to ensure paste command is completed

# Step 7: Press Enter
pyautogui.press('enter')