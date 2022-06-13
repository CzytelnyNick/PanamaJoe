from tkinter import *
from PIL import ImageTk, Image

pmap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    []
]


# class Map():
    # def __init__(self, root):
    #     self.root = root

def draw(frame):
    crow = 0
    for row in pmap:
        ccol = 0
        for col in row:
            generateBlock(ccol, crow, col, frame)
            ccol += 1
        crow += 1

def generateBlock(x, y, sym, frame):
    print(frame)
    img = ImageTk.PhotoImage(Image.open("brick.png"))

    label = Label(frame, image = img)
    label.pack()

        # else:
        #     img = ImageTk.PhotoImage(Image.open("pos2.png"))

# win = Tk()

# frame = Frame(win, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)


# a = Map(win)
# a.draw()

# win.mainloop()

# Import required libraries
# from tkinter import *
# from PIL import ImageTk, Image

# Create an instance of tkinter window
# win = Tk()

# Define the geometry of the window
# win.geometry("700x500")

# frame = Frame(win, width=600, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk

# win.mainloop()