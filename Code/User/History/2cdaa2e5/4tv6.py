from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests

# button commands
def user_message(entry):
    m = entry.get()
    return m
def quit():
    window.destroy()
    global quit_message
    quit_message = True

# AI commands
def message(character, message):
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
    global character_response
    character_response = response.json()['choices'][0]['message']

# window protocols
def on_closing():
    messagebox.showwarning("Quit", "Use the end conversation button to close the application, or your conversation will not be saved!")

# Global variables
character = "Assistant"

# GUI functions
def gen_window():
    global window
    window = Tk()
    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure('TButton', background='purple')
    window.protocol('WM_DELETE_WINDOW', on_closing)
    window.title("Character name, chat history file name")
    window.configure(background="black")
    frame = Frame(window)
    frame.pack()
    quit_button = ttk.Button(window, text = "End conversation", command = quit)
    quit_button.pack()
    window.mainloop()

while True:
    window = gen_window()
    quit_message = False
    message_entry = ttk.Entry(window)
    message_entry.pack()
    message_entry.bind("<Return>", lambda event: message(character, user_message(message_entry)))
    while True:
        try:
            gui_response = ttk.Label(text=character_response)
            gui_response.pack
        except:
            pass
        else:
            break