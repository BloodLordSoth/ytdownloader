import customtkinter, time
from tkinter import *
from pytubefix import YouTube


root = customtkinter.CTk()
root.title = ("Youtube video downloader")
root.iconname('images/soth.png')
image_path = PhotoImage(file='~/projects/github/ytdownloader/images/stcker.png')
bgimage = customtkinter.CTkLabel(root, image=image_path)
bgimage.place(relwidth=1.2, relheight=1.2, relx=-0.1, rely=-0.2)

root.geometry("550x500")
customtkinter.set_appearance_mode('dark')

thing = ''

def dl_vid():
    thing = entry.get()
    time.sleep(1)
    change_label.configure(text='Downloading . . .')
    time.sleep(1)
    yt = YouTube(thing)
    yt.streams.get_lowest_resolution().download()
    change_label.configure(text='Download successful')
    time.sleep(1)
    

entry = customtkinter.CTkEntry(root, width=300, placeholder_text='Paste URL here...')
entry.place(relx=0.2, rely=0.7)
button = customtkinter.CTkButton(root, text="Click to download", command=dl_vid)
button.place(relx=0.35, rely=0.75)
change_label = customtkinter.CTkLabel(root, width=200, height=30, text="Waiting for Link..." )
change_label.place(relx=0.3, rely=0.82)
label = customtkinter.CTkLabel(root, text="Charles x Philippa forever")
label.place(relx=0.72, rely=0.95)

root.mainloop()




