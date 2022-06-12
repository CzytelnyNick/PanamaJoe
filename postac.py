import tkinter as tk

# Creating the root window
root = tk.Tk()

# creating the Label with
# the text Middle
Label_middle = tk.Label(root,
                        text='Middle')

# Placing the Label at
# the middle of the root window
# relx and rely should be properly
# set to position the label on
# root window
Label_middle.place(relx=1,
                   rely=1,
                   anchor='center')
# Execute Tkinter
root.mainloop()