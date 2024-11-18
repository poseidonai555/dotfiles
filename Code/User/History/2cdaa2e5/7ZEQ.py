from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests
import time

# AI functions
def message(character, message, message_count, last_message_count):
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": character,
        "messages": [{"role": "user", "content": message}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    character_response = response.json()['choices'][0]['message']
    return character_response

window = Tk()
style = ttk.Style(window)
style.theme_use("clam")
style.configure('TButton', background='purple')
window.title("Character name, chat history file name")
window.configure(background="black")
frame = Frame(window)
frame.pack()
message_entry = ttk.Entry(window)
message_entry.pack()
quit_button = ttk.Button(window, text = "End conversation", command = quit)
quit_button.pack()
window.mainloop()
