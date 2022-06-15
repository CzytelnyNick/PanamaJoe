from json import load
from tkinter import *
from PIL import Image, ImageTk
import asyncio
import time

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("900x900")
canvas = Canvas(win, width=900, height=900, bg="black")
canvas.pack(pady=20)

fps = 60

pmap = [[
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1
],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 0, 0, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 3, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ],
        [
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0
        ],
        [
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0
        ],
        [
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0
        ],
        [
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 4, 0, 0, 0, 0, 0
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 1, 1, 0, 0, 1, 1,
            1, 1, 2, 1, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 2, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            7, 7, 0, 0, 0, 0, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 0, 0, 1, 1, 1, 1, 1, 1
        ],
        [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ]]
blocks = {
    1: {
        "img": "brick.png",
        "solid": "true",
        "climb": "false"
    },
    2: {
        "img": "ladder.png",
        "solid": "false",
        "climb": "true"
    },
    3: {
        "img": "pipe.png",
        "solid": "false",
        "climb": "true"
    },
    4: {
        "img": "doors.png",
        "solid": "true",
        "climb": "false"
    },
    5: {
        "img": "platform.png",
        "solid": "true",
        "climb": "false"
    },
    6: {
        "img": "fire1.png",
        "solid": "true",
        "climb": "false"
    },
    7: {
        "img": "fire2.png",
        "solid": "true",
        "climb": "false"
    }
}

for i in range(1, len(blocks) + 1):
    img = ImageTk.PhotoImage(Image.open(blocks[i]["img"]))
    blocks[i]["img"] = img

image = ImageTk.PhotoImage(Image.open('pos2.png'))
image2 = ImageTk.PhotoImage(Image.open('pos1.png'))

frame = Frame(win, width=10000, height=598)
frame.place(anchor='center', relx=0.5, rely=0.5)
frame.pack()

x = 15
y = 15

brick = ImageTk.PhotoImage(Image.open('brick.png'))


def generateBlock():
    for i in range(0, len(pmap)):
        for j in range(0, len(pmap[i])):
            if (pmap[i][j] != 0):
                print(blocks[pmap[i][j]]["solid"])
                canvas.create_image(j * 30,
                                    i * 30,
                                    anchor=NW,
                                    image=blocks[pmap[i][j]]["img"])


img = canvas.create_image(150, 195, anchor=NW, image=image)


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


async def gravity():
    if blocks[pmap[i][j]]["solid"] != "true":
        print("solid")
        return
        time.sleep(100)


async def load():
    generateBlock()


asyncio.run(load())


# asyncio.run(gravity())
# I want to make a dragon


win.mainloop()

#HALF OF CODE BY MR BOGDANIK(HE'S A REAL PROGRAMER) GITHUB: https://github.com/RobertBogdanik
