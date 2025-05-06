import customtkinter, time, sys, os
from tkinter import *
from pytubefix import YouTube


root = customtkinter.CTk()
root.title = ('Youtube video downloader')
root.geometry("500x200")
customtkinter.set_appearance_mode('dark')
root.resizable(width = False, height = False)


thing = ''

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundled .exe"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def dl_vid():
    change_label.configure(text='Downloading . . .')
    time.sleep(1)
    thing = entry.get()
    time.sleep(1)
    yt = YouTube(thing)
    yt.streams.get_highest_resolution().download()
    change_label.configure(text='Download successful')
    time.sleep(1)
    

entry = customtkinter.CTkEntry(root, width=300, placeholder_text='Paste URL here...')
entry.place(relx=0.2, rely=0.3)
button = customtkinter.CTkButton(root, text="Click to download", command=dl_vid)
button.place(relx=0.35, rely=0.5)
change_label = customtkinter.CTkLabel(root, width=200, height=30, text="Waiting for Link..." )
change_label.place(relx=0.3, rely=0.69)
label = customtkinter.CTkLabel(root, text="Charles x Philippa forever")
label.place(relx=0.70, rely=0.90)

root.mainloop()




