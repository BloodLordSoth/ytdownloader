import customtkinter, time, sys, os
from tkinter import *
from pytubefix import YouTube
from PIL import Image


root = customtkinter.CTk()
root.title('Youtube video downloader')
root.geometry("500x200")
customtkinter.set_appearance_mode('dark')
bg_image = customtkinter.CTkImage(Image.open("assets/ytdbg1.png"), size=(500, 200))
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
    
bg_label = customtkinter.CTkLabel(root, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
entry = customtkinter.CTkEntry(root, width=300, placeholder_text='Paste URL here...')
entry.place(relx=0.2, rely=0.38)
button = customtkinter.CTkButton(root, text="Click to download", command=dl_vid)
button.place(relx=0.35, rely=0.58)
change_label = customtkinter.CTkLabel(root, width=200, height=30, text="Waiting for Link..." )
change_label.place(relx=0.28, rely=0.77)
label = customtkinter.CTkLabel(root, text="Charles x Philippa forever")
label.place(relx=0.70, rely=0.90)
prop_label = customtkinter.CTkLabel(root, text="Art by SpasticFantastic")
prop_label.place(relx=0, rely=0.90)

root.mainloop()




