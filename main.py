from tkinter import *
from PIL import ImageTk, Image
import asyncio
import os

root = Tk()
root.configure(background='black')
img = ImageTk.PhotoImage(Image.open("pos1.png"))
img2 = ImageTk.PhotoImage(Image.open("pos2.png"))

# frame.pack()
root.geometry("300x200")
# panel = Label(root, image=img)
# panel2 = Label(root, image=img2)
myCanvas = Canvas(root, width = 600, height = 600, bg = "black")
myCanvas.pack(pady=20)

i = 0
x = 0
y = 0


def move(event):
    global x
    global y
    if event.keysym == 'Up':  # rozpoznanie strzałki do góry
        print("gora")
    elif event.keysym == 'Down':
        myCanvas.create_image(x, y, anchor=NW, image=img2, tags='my_tag')
    elif event.keysym == 'Left':

        myCanvas.delete('my_tag')

        myCanvas.create_image(x, y, anchor=NW, image=img, tags='my_tag')
        # panel.grid(row=3, column=3)

        x = x - 10
        print(x)

    elif event.keysym == 'Right':
        myCanvas.delete('my_tag')
        myCanvas.create_image(x, y, anchor=NW, image=img2, tags='my_tag')

        x = x + 10

        print(x)
        # panel2.pack(side="bottom", fill="both", expand="yes")


root.bind('<Key>', move)
root.mainloop()
