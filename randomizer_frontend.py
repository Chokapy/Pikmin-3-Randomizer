"""
Program name : randomizer_frontend.py
Author : Chokapi
Date : 08.04.2025
Modif : 08.04.2025
Version : 2.0
"""
#import of the backend
import randomizer_backend as bknd

#import of tkinter
from tkinter import *


def init_window():
    window.mainloop()

#variable
normal_font = 'TkDefaultFont 12'
button_font = 'TkDefaultFont 30'
#--------------------main window--------------------
window = Tk()
window.title("Pikmin 3 Randomizer")

#finding the screen with and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#size of the window
sizex = 500
sizey = 300

#finding the middle of the screen
posx = screen_width // 2 - (sizex // 2)
posy = screen_height // 2 - (sizey // 2)

#place the window in the middle
window.geometry(f"{sizex}x{sizey}+{posx}+{posy}")

#make the window not resizable
window.resizable(False, False)

#--------------------left side--------------------

frm_left = Frame(window)
frm_left.pack(side=LEFT, anchor="n", pady=10, padx=10)

text_left = [
        "Randomize enemies",
        "Randomize fruits",
        "Randomize plants",
        "Randomize onions",
        "No limit mode",
        "Ultra spicy mode"
        ]

frame_left = [None, None, None, None, None, None]

checkbox_left = [None, None, None, None, None, None]

var_left = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

label_left = [None, None, None, None, None, None]

for i in range(len(text_left)):
    frame_left[i] = Frame(frm_left, pady=5, padx=5)
    frame_left[i].pack(anchor="w")

    checkbox_left[i] = Checkbutton(frame_left[i], variable=var_left[i], onvalue=1, offvalue=0)
    checkbox_left[i].pack(side=LEFT)

    label_left[i] = Label(frame_left[i], text=text_left[i], font=normal_font)
    label_left[i].pack()

#--------------------right side--------------------

frm_right = LabelFrame(window)
frm_right.pack(side=RIGHT, anchor="n", pady=10, padx=10)

frame_right = [None, None, None, None]

button_right = [None, None, None]

for i in range(len(frame_right)):
    frame_right[i] = Frame(frm_right, pady=5, padx=5)
    frame_right[i].pack(anchor="e")

button_right[0] = Button(frame_right[0], text="🛈", font=button_font, height=0, width=2)
button_right[0].pack(padx=(5,0), side=RIGHT)

button_right[0] = Button(frame_right[0], text="📁", font=button_font, height=0, width=2)
button_right[0].pack(padx=(5,0), side=RIGHT)

button_right[0] = Button(frame_right[0], text="🌤", font=button_font, height=0, width=2)
button_right[0].pack(padx=(5,0), side=RIGHT)