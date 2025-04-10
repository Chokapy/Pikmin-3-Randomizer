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
button_font = 'TkDefaultFont 20'
#--------------------main window--------------------
window = Tk()
window.title("Pikmin 3 Randomizer")
window.configure(bg=bknd.dark_mode["background"])

#finding the screen with and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#size of the window
sizex = 500
sizey = 320

#finding the middle of the screen
posx = screen_width // 2 - (sizex // 2)
posy = screen_height // 2 - (sizey // 2)

#place the window in the middle
window.geometry(f"{sizex}x{sizey}+{posx}+{posy}")

#make the window not resizable
window.resizable(False, False)

frm_option = Frame(window, bg=bknd.dark_mode["background"])
frm_option.pack(fill="x")
#--------------------left side--------------------

frm_left = Frame(frm_option, bg=bknd.dark_mode["background"])
frm_left.pack(side=LEFT, anchor="n", pady=10, padx=10)

text_left = [
        "Randomize enemies",
        "Randomize fruits",
        "Randomize plants",
        "Randomize onions",
        "No limit mode",
        "Hard mode"
        ]

frame_left = [None, None, None, None, None, None]

checkbox_left = [None, None, None, None, None, None]

var_left = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

label_left = [None, None, None, None, None, None]

for i in range(len(text_left)):
    frame_left[i] = Frame(frm_left, pady=5, padx=5, bg=bknd.dark_mode["background"])
    frame_left[i].pack(anchor="w")

    checkbox_left[i] = Checkbutton(frame_left[i], variable=var_left[i], onvalue=1, offvalue=0, bg=bknd.dark_mode["background"])
    checkbox_left[i].pack(side=LEFT)

    label_left[i] = Label(frame_left[i], text=text_left[i], font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
    label_left[i].pack()

#--------------------right side--------------------

frm_right = Frame(frm_option, bg=bknd.dark_mode["background"])
frm_right.pack(side=RIGHT, anchor="n", pady=10, padx=10)

frame_right = [None, None, None, None]

button_right = [None, None, None]

for i in range(len(frame_right)):
    frame_right[i] = Frame(frm_right, pady=5, padx=5, bg=bknd.dark_mode["background"])
    frame_right[i].pack(anchor="w", fill="x")

button_right[0] = Button(frame_right[0], text="ℹ", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
button_right[0].pack(padx=(5,0), side=RIGHT)

button_right[0] = Button(frame_right[0], text="📁", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
button_right[0].pack(padx=(5,0), side=RIGHT)

button_right[0] = Button(frame_right[0], text="🌤", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
button_right[0].pack(padx=(5,0), side=RIGHT)

lbl_seed = Label(frame_right[1], text="Seed", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_seed.pack(padx=5, side=LEFT)

ent_seed = Entry(frame_right[1], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_seed.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)

var_gennum = IntVar()

ckbx_gennum = Checkbutton(frame_right[2], variable=var_gennum, onvalue=1, offvalue=0, bg=bknd.dark_mode["background"])
ckbx_gennum.pack(side=LEFT)

lbl_gennum = Label(frame_right[2], text="Max gen num", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_gennum.pack(side=LEFT, padx=(5,0))

ent_gennum = Entry(frame_right[2], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_gennum.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)

lbl_stonion = Label(frame_right[3], text="First onion", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_stonion.pack(side=LEFT, padx=(5,0))

ent_stonion = Entry(frame_right[3], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_stonion.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)

#--------------------bottom button--------------------

frm_bottom = Frame(window, bg=bknd.dark_mode["background"])
frm_bottom.pack(padx=10)

btn_randomize = Button(frm_bottom, text="RANDOMIZE", font=button_font, width=12, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
btn_randomize.pack(side=LEFT, padx=10)

btn_pack = Button(frm_bottom, text="PACK", font=button_font, width=12, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
btn_pack.pack(side=RIGHT, padx=10)