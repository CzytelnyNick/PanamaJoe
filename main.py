from tkinter import *
from PIL import Image, ImageTk


pmap = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    ]

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("900x1000")

canvas = Canvas(win, width=1000, height=900, bg="black")
canvas.pack(pady=20)

image = ImageTk.PhotoImage(Image.open('pos2.png'))
image2 = ImageTk.PhotoImage(Image.open('pos1.png'))
img = canvas.create_image(150, 195, anchor=NW, image=image)


frame = Frame(win, width=10000, height=598)
frame.place(anchor='center', relx=0.5, rely=0.5)
frame.pack()

def left(e):
   x = -15
   y = 0
   canvas.itemconfig(img, image=image2)
   canvas.move(img, x, y)

def right(e):
   x = 15
   y = 0
   canvas.itemconfig(img, image=image)
   canvas.move(img, x, y)

def up(e):
   x = 0
   y = -15
   canvas.move(img, x, y)

def down(e):
   x = 0
   y = 15
   # if x < 150 or x > 250:
   #     canvas.itemconfig(150, 195)
   canvas.move(img, x, y)

# Bind the move function
win.bind("<Left>", left)
win.bind("<Right>", right)
win.bind("<Up>", up)
win.bind("<Down>", down)

brick = ImageTk.PhotoImage(Image.open("brick.png"))
door = ImageTk.PhotoImage(Image.open("doors.png"))
pipe = ImageTk.PhotoImage(Image.open("pipe.png"))
ladder = ImageTk.PhotoImage(Image.open("ladder.png"))
platform = ImageTk.PhotoImage(Image.open("platform.png"))
fireB = ImageTk.PhotoImage(Image.open("fire1.png"))
fireL = ImageTk.PhotoImage(Image.open("fire2.png"))
def generateBlock(x, y, col):
   if col == 1:
    canvas.create_image(x*30, y*30, anchor=NW, image=brick)
   elif col == 2:
    canvas.create_image(x*30, y*30, anchor=NW, image=ladder)
   elif col == 3:
    canvas.create_image(x*31, y*30, anchor=NW, image=pipe)
   elif col == 4:
    canvas.create_image(x * 30, y * 30, anchor=NW, image=door)
   elif col == 5:
    canvas.create_image(x * 30, y * 30, anchor=NW, image=platform)
   elif col == 6:
       canvas.create_image(x * 30, y * 30, anchor=NW, image=fireB)
   elif col == 7:
       canvas.create_image(x * 30, y * 30, anchor=NW, image=fireL)
crow = 0
for row in pmap:
   ccol = 0
   for col in row:
         generateBlock(ccol, crow, col)
         ccol += 1
   crow += 1

win.mainloop()


#HALF OF CODE BY MR BOGDANIK(HE'S A REAL PROGRAMER) GITHUB: https://github.com/RobertBogdanik