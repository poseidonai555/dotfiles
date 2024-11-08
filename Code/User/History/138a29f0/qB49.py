import os
import json
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import Frame
from tkinter import messagebox
import requests
import yaml


#General functions
def character_input():#edit this after (is_fictional_character)
    def submit_button():
        global character
        character = entry.get()
        character = character.lower()
        if character == "":
            messagebox.showerror("Error", "Field cannot be left blanc")
        elif character.isdigit() == True:
            messagebox.showerror("Error", "Cannot be a number")
        elif isinstance(character, str) != True :
            messagebox.showerror("Error", "Character is not string")
        elif character in characters:
            messagebox.showerror("Error", "Character already exists")
        else:
            """
            GPT3 is_fictional_character
            """
            '''
            if is_fictional_character() != True:
                    messagebox.showerror("Error", "must be a fictional character")
            else:
            '''
            characters.append(character)
            save_history()
            character_json_file()
            os.makedirs(r'character_data/character_history/'+character)
    #GUI
    clear_window()
    entry = ttk.Entry(window)
    entry.pack()
    entry.bind("<Return>", lambda event: submit_button())
    submit_butn = ttk.Button(window, text = "Submit character name", command=submit_button)
    submit_butn.pack()
def read_characters_file():
    global characters
    characters = []
    with open(r'character_names.txt', 'r') as file:
        for line in file:
            characters.append(line.strip())
def write_characters_file():#edit this after (character_history)
    with open(r'character_names.txt', 'w') as file:
        for item in characters:
            file.write(item+'\n')
def save_history():
    clear_window()
    def submit_button():
        global file_name
        file_name = entry.get()
        if file_name == "":
            messagebox.showerror("Error", "Field cannot be left blanc")
        else:
            with open((r'character_data/character_history/'+character+"/"+file_name+'_history.json'), 'w') as file: #creates the history file
                dictionary = {}
                dictionary["data"] = character_history
                yaml.dump(dictionary, file) #adds data to history file
            with open((r'character_data/character_history/'+character+"/"+character+'_file_names.txt'), 'w') as file:
                file.write(file_name)
            window.destroy()
    #GUI
    entry = ttk.Entry(window)
    entry.pack()
    entry.bind("<Return>", lambda event: submit_button())
    submit_butn = ttk.Button(window, text = "submit history file name", command = submit_button)
    submit_butn.pack()
def character_json_file():#create pygmalion .yaml file, add a greeting toggle/
    personality = "personality" #personality_character()
    looks = "looks" #looks_character()
    senario = "scenario" #senario_character()
    example_messages = "example messages" #example_messages_character()
    summary = "summary" #summary_character()

    character_data = {
        "name": character,
        "context:": summary_character()+" "+personality_character()+" "+looks_character()+" "+'\n'+example_messages_character()
    }
    
    with open((r'/home/poseidon/text-generation-webui/characters/'+character+".yaml"), 'w') as file:
        yaml.dump(character_data, file)

    save_history()

def file_name_list():
    with open((r'character_data/character_history/'+character_menu_choice+"/"+character_menu_choice+'_file_names.txt'), 'r') as file:
        global file_names
        file_names = []
        for line in file:
            file_names.append(line.strip())
def write_histories():
    with open(r'character_data/character_history/'+character_menu_choice+"/"+character_menu_choice+'_file_names.txt', 'w') as file:
        file.truncate(0)
        for item in file_names:
            file.write(item+'\n')

#GUI functions
def on_closing():
    messagebox.showwarning("Quit", "Use the quit program button to close the application, or characters wont be saved!")
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

#AI functions
def is_fictional_character():
    #info for requests module

    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": "Assistant",
        "messages": [{"role": "user", "content": ("is "+character+" a fictional character, answer in one word")}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    if "yes" in assistant_message or "Yes" in assistant_message:
        return True
    else:
        return False
def summary_character():
        #info for requests module
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": "Assistant",
        "messages": [{"role": "user", "content": ('''write 10 words to summarize the most important attributes of '''+character)}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    return str(assistant_message)
def looks_character():
        #info for requests module
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": "Assistant",
        "messages": [{"role": "user", "content": ('''write 170 words about the personality of '''+character)}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    return str(assistant_message)
def personality_character():
        #info for requests module
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": "Assistant",
        "messages": [{"role": "user", "content": ('''write 170 words about the looks of '''+character)}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    return str(assistant_message)
def example_messages_character():
        #info for requests module
    url = "http://127.0.0.1:5000/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "mode": "chat",
        "character": "Assistant",
        "messages": [{"role": "user", "content": ('''write a 220 words of example messages of '''+character+'''with a user, give this in the format '''+character+''': message, user: message''')}]
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    assistant_message = response.json()['choices'][0]['message']['content']
    return str(assistant_message)
def message_character():
    messages = []
    def chat():
        user_input = input("")
        #info for requests module
        url = "http://127.0.0.1:5000/v1/chat/completions"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "mode": "chat",
            "character": "Assistant",
            "messages": [{"role": "user", "content": user_input}]
        }
        response = requests.post(url, headers=headers, json=data, verify=False)
        character_message = response.json()['choices'][0]['message']['content']
        print(character_message)
        messages.append(user_input, character_message)
    def quit():
        return True
    while quit() == False:
        chat()
       
    #GUI
    clear_window()
    entry = ttk.Entry(window)
    entry.pack
    entry.bind("<Return>", lambda event: chat())
    send_butn = ttk.Button(window, text = "Send", command = chat)
    send_butn.pack()
    quit_butn = ttk.Button(window, text = "Save and close chat")
    quit_butn.pack()
    quit_butn.bind("<Return>", lambda event: quit())

#data that must be obtained before program is run
read_characters_file()
#character's pygmalion history must be defined here
character_history = "testing 123"

while True:
    #if list is empty
    if not characters:
        quit_GUI = False
        #functions for the buttons
        def create_new_character():
            character_input()
            #persona json file
            #redirect to pygmalion
            #once done with chat
        def quit_program():
            write_characters_file()
            window.destroy()
            global quit_GUI
            quit_GUI = True
        #GUI
        window = Tk()
        #GUI style
        style = ttk.Style(window)
        style.theme_use("clam")
        style.configure('TButton', background='purple')
        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.geometry("2560x1440")
        window.title("Character Creation")
        window.configure(background='black')
        frame = Frame(window)
        frame.pack()
        CNC_button = ttk.Button(window, text = "Create new character", command=create_new_character)
        QUIT_button = ttk.Button(window, text = "Quit program", command=quit_program)
        CNC_button.pack(padx=10, pady=10)
        QUIT_button.pack(padx = 10, pady = 10)
        window.mainloop()
        if quit_GUI == True:
            break
    #saved characters
    else:
        #menu (characters saved)
        quit_GUI = False
        #functions for the buttons
        def choose_from_characters():
            clear_window()
            #chose pre existing character option
            window.title("Character Menu")
            def add_to_choice(a):
                global character_menu_choice
                character_menu_choice = a
                #GUI for options with choosen character
                clear_window()
                def load_chat_history_with(): #Make sure appended chat history is on a new line
                    file_name_list()
                    if len(file_names) == 0:
                        messagebox.showerror("Error", "No histories to load from")
                    else:
                        file_name_list()
                        clear_window()
                        window.title("Histories menu")
                        def choice(b):
                            global histories_menu_choice
                            histories_menu_choice = b
                            with open((r'character_data/character_history/'+character_menu_choice+"/"+histories_menu_choice+'_history.json'), 'r') as file:
                                file_data = json.load(file)
                            file_data["data"] = file_data["data"] + " " + character_history
                            with open((r'character_data/character_history/'+character_menu_choice+"/"+histories_menu_choice+'_history.json'), 'w') as file:
                                3(file_data, file)
                            window.destroy()
                        for b in file_names:
                            button = ttk.Button(window, text = b, command=lambda b=b:choice(b))
                            button.pack(padx=10, pady=10)
                def delete_chat_history_with():
                    file_name_list()
                    if len(file_names) == 0:
                        messagebox.showinfo(message="no histories to delete")
                    elif len(file_names) == 1:
                        confirm = messagebox.askquestion(message="Are you sure you want to delete "+file_names[0]+"?", type=messagebox.YESNO)
                        if confirm == "yes":
                            os.remove(r'character_data/character_history/'+character_menu_choice+"/"+file_names[0]+'_history.json')
                            file_names.remove(file_names[0])
                            write_histories()
                            messagebox.showinfo(message="Deleted")
                            window.destroy()
                        else:
                            messagebox.showinfo(message=file_names[0]+" has not been deleted")
                            window.destroy()
                    else:
                        file_name_list()
                        clear_window()
                        window.title("Histories menu")
                        def choice(c):
                            global histories_menu_choice
                            histories_menu_choice = c
                            confirm = messagebox.askquestion(message="Are you sure you want to delete "+histories_menu_choice)
                            if confirm == "yes":
                                os.remove(r'character_data/character_history/'+character_menu_choice+"/"+histories_menu_choice+'_history.json')
                                file_names.remove(histories_menu_choice)
                                with open(r'character_data/character_history/'+character_menu_choice+"/"+character_menu_choice+'_file_names.txt', 'w') as file:
                                    file.truncate(0)
                                    for item in file_names:
                                        file.write(item+'\n')
                                window.destroy()
                            else:
                                messagebox.showinfo(message=histories_menu_choice+" has not been deleted")
                                window.destroy()
                        for c in file_names:
                            button = ttk.Button(window, text= c, command=lambda c=c: choice(c))
                            button.pack(padx=10, pady=10)
                def create_a_new_chat_history_with():
                    #redirect to pygmalion
                    #pygmailion needs files char_persona file
                    #create new history save
                    file_name_list()
                    def submit_button():
                        history_save_name = entry.get()
                        if history_save_name == "":
                            messagebox.showerror("Error", "Field cannot be left blanc")
                        elif history_save_name in file_names:
                            messagebox.showerror("Error", "File name already exists")
                        else:
                            with open((r'character_data/character_history/'+character_menu_choice+"/"+history_save_name+'_history.json'), 'w') as file: #creates the history file
                                dictionary = {}
                                dictionary["data"] = character_history
                                yaml.dump(dictionary, file) #adds data to history file
                            file_names.append(history_save_name)
                            write_histories()
                            window.destroy()
                    clear_window()
                    entry = ttk.Entry(window)
                    entry.pack()
                    entry.bind("<Return>", lambda event: submit_button())
                    submit_butn = ttk.Button(window, text= "Submit history name", command= submit_button)
                    submit_butn.pack()
                LCHW_button = ttk.Button(window, text= "Load chat history with " + character_menu_choice, command=load_chat_history_with)
                DCHW_button = ttk.Button(window, text= "Delete chat history with "+character_menu_choice, command=delete_chat_history_with)
                CANCHW_button = ttk.Button(window, text= "Create a new chat history with "+character_menu_choice+" and do not delete any old chat histories", command=create_a_new_chat_history_with)
                LCHW_button.pack(padx=10, pady=10)
                DCHW_button.pack(padx=10, pady=10)
                CANCHW_button.pack(padx=10, pady=10)
            for a in characters:
                button = ttk.Button(window, text= a, command=lambda char=a:add_to_choice(char))
                button.pack(padx=10, pady=10)
        def create_new_character():
            character_input()
            #redirect to pygmalion
            #once done with chat
        def delete_character():
            if len(characters) == 1:
                confirm = messagebox.askquestion(message="Are you sure you want to delete "+characters[0], type=messagebox.YESNO)
                if confirm == "yes":
                    os.remove((r'/home/poseidon/text-generation-webui/characters/'+characters[0]+'.yaml'))
                    shutil.rmtree(('character_data/character_history/'+characters[0]))
                    messagebox.showinfo(message= characters[0]+" deleted")
                    del characters[characters.index(characters[0])]
                    window.destroy()
                else:
                    messagebox.showinfo(message=characters[0]+" has not been deleted")
                    window.destroy()
            else:
                clear_window()
                window.title("Character Menu")
                def add_to_choice(x):
                        global character_menu_choice
                        character_menu_choice = x#error here, always chooses the last character in the list
                        confirm = messagebox.askquestion(message="Are you sure you want to delete "+character_menu_choice+"?", type=messagebox.YESNO)
                        if confirm == "yes":
                            del characters[characters.index(character_menu_choice)]
                            os.remove((r'/home/poseidon/text-generation-webui/characters/'+character_menu_choice+'.json'))
                            shutil.rmtree(('character_data/character_history/'+character_menu_choice))
                            messagebox.showinfo(message= character_menu_choice+" deleted")
                            window.destroy()
                        else:
                            messagebox.showinfo(message= character_menu_choice+" has not been deleted")
                            window.destroy()
                for x in characters:
                    button = ttk.Button(window, text= x, command= lambda char=x:add_to_choice(char))
                    button.pack(padx=10, pady=10)
        def quit_program():
            write_characters_file()
            window.destroy()
            global quit_GUI
            quit_GUI = True
        #GUI
        window = Tk()
        #GUI style
        style = ttk.Style(window)
        style.theme_use("clam")
        style.configure('TButton', background='purple')
        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.geometry("2560x1440")
        window.title("Main menu")
        window.configure(background='black')
        frame = Frame(window)
        frame.pack()
        CFC_button = ttk.Button(window, text = "Choose from characters", command=choose_from_characters)
        CNC_button = ttk.Button(window, text = "Create new character", command=create_new_character)
        DC_button = ttk.Button(window, text = "Delete character", command=delete_character)
        QUIT_button = ttk.Button(window, text = "Quit program", command=quit_program)
        CFC_button.pack(padx=10, pady=10)
        CNC_button.pack(padx=10, pady=10)
        DC_button.pack(padx=10, pady=10)
        QUIT_button.pack(padx=10, pady=10)
        window.mainloop()
        if quit_GUI == True:
            break
