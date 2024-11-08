from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests

# Procedures
def check_if_message():
    

# button functions
def user_message(entry):
    m = entry.get()
    return m
def quit():
    window.destroy()
    global quit_message
    quit_message = True

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
    if message_count == last_message_count:
        return character_response
    else:
        return "Please wait for the character to reply" # change this to be the character's name. 
    message_count +=1 
    return character_response

# window protocols
def on_closing():
    messagebox.showwarning("Quit", "Use the end conversation button to close the application, or your conversation will not be saved!")

# Global variables
character = "Assistant"
message_count = 0
last_message_count = 0

# GUI functions
def gen_window():
    global window

while True:
    quit_message = False
    window = Tk()
    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure('TButton', background='purple')
    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.title("Character name, chat history file name")
    window.configure(background="black")
    frame = Frame(window)
    frame.pack()
    message_entry = ttk.Entry(window)
    message_entry.pack()
    message_entry.bind("<Return>", lambda event: message(character, user_message(message_entry)))
    quit_button = ttk.Button(window, text = "End conversation", command = quit)
    quit_button.pack()
    window.mainloop()