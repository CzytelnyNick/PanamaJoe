from tkinter import *
from PIL import ImageTk, Image
import asyncio
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("pos1.png"))
img2 = ImageTk.PhotoImage(Image.open("pos2.png"))
frame = Frame(root)
root.geometry("200x200")
# panel = Label(root, image=img)
# panel2 = Label(root, image=img2)

panel = Label(root, image=img)
panel2 = Label(root, image=img2)
x = 0
y = 0
def move(event):
    if event.keysym == 'Up':  # rozpoznanie strzałki do góry
        print("gora")
    elif event.keysym == 'Down':
        print("dol")
    elif event.keysym == 'Left':

        frame.pack_forget()
        panel.pack(side="bottom", fill="both", expand="yes")

        print("test")

    elif event.keysym == 'Right':

        frame.pack_forget()
        panel2.pack(side="bottom", fill="both", expand="yes")


        print("test")
        # panel2.pack(side="bottom", fill="both", expand="yes")





root.bind('<Key>', move)
root.mainloop()
