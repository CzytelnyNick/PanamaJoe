from tkinter import *
from PIL import ImageTk, Image
import asyncio
import os
async def main():
    root = Tk()
    img = ImageTk.PhotoImage(Image.open("pos1.png"))
    img2 = ImageTk.PhotoImage(Image.open("pos2.png"))
    root.geometry("200x200")
    panel = Label(root, image = img)
    panel2 = Label(root, image = img2)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    await asyncio.sleep(2)
    panel2.pack(side = "top", fill = "", expand = "yes")
    root.mainloop()
asyncio.run(main())
