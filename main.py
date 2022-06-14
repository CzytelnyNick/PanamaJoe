# from tkinter import *
# from PIL import ImageTk, Image
# import asyncio
# import os
from map import *

# root = Tk()
# root.configure(background='black')
# img = ImageTk.PhotoImage(Image.open("pos1.png"))
# img2 = ImageTk.PhotoImage(Image.open("pos2.png"))

# root.geometry("300x200")
# # myCanvas = Canvas(root, width = 600, height = 600, bg = "black")

# player = Label(image=img)
# player.pack()

# i = 0
# x = 500
# y = 100



# def move(event):
#     global x
#     global y
#     # if event.keysym == 'Up':  # rozpoznanie strzałki do góry
#     #     print("gora")
#     # elif event.keysym == 'Down':
#     #     myCanvas.create_image(x, y, anchor=NW, image=img2, tags='my_tag')
#     if event.keysym == 'Left':

#         # myCanvas.delete('my_tag')

#         # myCanvas.create_image(x, y, anchor=NW, image=img, tags='my_tag')
#         # panel.grid(row=3, column=3)
#         # player.config(x=x, y=y)

#         x = x - 10
#         # player.config(padx=x, image=img)
#         player.pack(padx=x, pady=y)
#         print(x)

#     elif event.keysym == 'Right':
#         # myCanvas.delete('my_tag')
#         # myCanvas.create_image(x, y, anchor=NW, image=img2, tags='my_tag')

#         x = x + 10

#         print(x)
#         # panel2.pack(side="bottom", fill="both", expand="yes")



# root.bind('<Key>', move)
# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# # Define a Canvas widget
canvas = Canvas(win, width=600, height=400, bg="white")
canvas.pack(pady=20)

# # Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('pos1.png'))
img = canvas.create_image(250, 120, anchor=NW, image=image)

frame = Frame(win, width=600, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)
frame.pack()

def left(e):
   x = -20
   y = 0
   canvas.move(img, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(img, x, y)

# Bind the move function
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)



brick = ImageTk.PhotoImage(Image.open("brick.png"))


map = PJM(frame)
map.draw()




# def draw():
#     crow = 0
#     for row in pmap:
#         ccol = 0
#         for col in row:
#             generateBlock(ccol, crow, col)
#             ccol += 1
#         crow += 1

# def generateBlock(img):
#     global frame
#     global ImageTk
#     global PhotoImage

#     global Image
    
#     label = Label(frame, text="Hello World", width=10)
#     label.pack()

#     print(img)
#     label = Label(frame, image = img)
#     print(label)
#     label.pack()

# draw()\
# generateBlock(brick)
win.mainloop()