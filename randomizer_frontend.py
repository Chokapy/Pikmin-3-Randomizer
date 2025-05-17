"""
Program name : randomizer_frontend.py
Author : Chokapi
Date : 08.04.2025
Modif : 11.04.2025
Version : 2.0
"""
#import of the backend
import randomizer_backend as bknd

#import of tkinter
from tkinter import *

#variable
normal_font = 'TkDefaultFont 12'
button_font = 'TkDefaultFont 20'

current_mode = "dark"

background_element = []
widget_element = []

def init_window():
    window.mainloop()


def randomize():
    if var_left[0].get():
        bknd.randomize_all(bknd.gen_folder, bknd.enemies_to_replace, bknd.enemies_list)

    if var_left[1].get():
        bknd.randomize_all(bknd.gen_folder, bknd.fruits_to_replace, bknd.fruits_list)

    if var_left[2].get():
        bknd.randomize_all(bknd.gen_folder, bknd.plants_to_replace, bknd.plants_list)


def darklight_mode(background_list, widget_list):
    global current_mode

    #check what the current mode is and change it
    if current_mode == "dark":
        color = bknd.light_mode
        text = "🌙"
        current_mode = "light"
    else:
        color = bknd.dark_mode
        text = "🌤"
        current_mode = "dark"

    #edit every background element
    for i in range(len(background_list)):
        #look if object not a list
        if not isinstance(background_list[i], list):
            #look if the element have text
            try:
                background_list[i].configure(bg=color["background"], fg=color["text"])
            except TclError:
                background_list[i].configure(bg=color["background"])
        else:
            #edit 2d list
            for j in range(len(background_list[i])):
                #look if the element have text
                try:
                    background_list[i][j].configure(bg=color["background"], fg=color["text"])
                except TclError:
                    background_list[i][j].configure(bg=color["background"])

    # edit every widget element
    for i in range(len(widget_list)):
        # look if object not a list
        if not isinstance(widget_list[i], list):
            # look if the element have text
            try:
                widget_list[i].configure(bg=color["widget"], fg=color["text"])
            except TclError:
                widget_list[i].configure(bg=color["widget"])
        else:
            # edit 2d list
            for j in range(len(widget_list[i])):
                # look if the element have text
                try:
                    widget_list[i][j].configure(bg=color["widget"], fg=color["text"])
                except TclError:
                    widget_list[i][j].configure(bg=color["widget"])

    widget_list[0][2].configure(text=text)


def create_info_window():
    global current_mode
    if current_mode == "dark":
        color = bknd.dark_mode
    else:
        color = bknd.light_mode

    info = Toplevel()
    info.title("Pikmin 3 Randomizer Info")
    info.configure(bg=color["background"])

    # finding the screen with and height
    screen_width = info.winfo_screenwidth()
    screen_height = info.winfo_screenheight()

    # size of the window
    sizex = 500
    sizey = 320

    # finding the middle of the screen
    posx = screen_width // 2 - (sizex // 2)
    posy = screen_height // 2 - (sizey // 2)

    # place the window in the middle
    info.geometry(f"{sizex}x{sizey}+{posx}+{posy}")

    # make the window not resizable
    info.resizable(False, False)

#--------------------main window--------------------
window = Tk()
window.title("Pikmin 3 Randomizer")
window.configure(bg=bknd.dark_mode["background"])
background_element.append(window)

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
background_element.append(frm_option)

#--------------------left side--------------------

frm_left = Frame(frm_option, bg=bknd.dark_mode["background"])
frm_left.pack(side=LEFT, anchor="n", pady=10, padx=10)
background_element.append(frm_left)

text_left = [
        "Randomize enemies",
        "Randomize fruits",
        "Randomize plants",
        "Randomize onions",
        "Open progression",
        "True Spice"
        ]

frame_left = [None, None, None, None, None, None]
background_element.append(frame_left)

checkbox_left = [None, None, None, None, None, None]
background_element.append(checkbox_left)

var_left = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

label_left = [None, None, None, None, None, None]
background_element.append(label_left)

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
background_element.append(frm_right)

frame_right = [None, None, None, None, None]
background_element.append(frame_right)

button_right = [None, None, None]
widget_element.append(button_right)

for i in range(len(frame_right)):
    frame_right[i] = Frame(frm_right, pady=5, padx=5, bg=bknd.dark_mode["background"])
    frame_right[i].pack(anchor="w", fill="x")

button_right[0] = Button(frame_right[0], text="ℹ", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"], command=create_info_window)
button_right[0].pack(padx=(5,0), side=RIGHT)

button_right[1] = Button(frame_right[0], text="📁", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"], command=bknd.open_mod_folder)
button_right[1].pack(padx=(5,0), side=RIGHT)

button_right[2] = Button(frame_right[0], text="🌤", font=button_font, width=3, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"], command=lambda: darklight_mode(background_element, widget_element))
button_right[2].pack(padx=(5,0), side=RIGHT)

var_chaos = IntVar()

ckbx_chaos = Checkbutton(frame_right[1], variable=var_chaos, onvalue=1, offvalue=0, bg=bknd.dark_mode["background"])
ckbx_chaos.pack(side=LEFT)
background_element.append(ckbx_chaos)

lbl_chaos = Label(frame_right[1], text="Chaos Randomizer", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_chaos.pack(side=LEFT, padx=(5,0))
background_element.append(lbl_chaos)

var_iron = IntVar()

ckbx_iron = Checkbutton(frame_right[2], variable=var_iron, onvalue=1, offvalue=0, bg=bknd.dark_mode["background"])
ckbx_iron.pack(side=LEFT)
background_element.append(ckbx_iron)

lbl_iron = Label(frame_right[2], text="Iron-min Challenge", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_iron.pack(padx=5, side=LEFT)
background_element.append(lbl_iron)

ent_iron = Entry(frame_right[2], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_iron.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)
widget_element.append(ent_iron)

var_gennum = IntVar()

ckbx_gennum = Checkbutton(frame_right[3], variable=var_gennum, onvalue=1, offvalue=0, bg=bknd.dark_mode["background"])
ckbx_gennum.pack(side=LEFT)
background_element.append(ckbx_gennum)

lbl_gennum = Label(frame_right[3], text="Max gen num", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_gennum.pack(side=LEFT, padx=(5,0))
background_element.append(lbl_gennum)

ent_gennum = Entry(frame_right[3], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_gennum.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)
widget_element.append(ent_gennum)

lbl_stonion = Label(frame_right[4], text="First onion", font=normal_font, bg=bknd.dark_mode["background"], fg=bknd.dark_mode["text"])
lbl_stonion.pack(side=LEFT, padx=(5,0))
background_element.append(lbl_stonion)

ent_stonion = Entry(frame_right[4], font=normal_font, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
ent_stonion.pack(padx=(5,0), side=RIGHT, fill="x", expand=True)
widget_element.append(ent_stonion)

#--------------------bottom button--------------------

frm_bottom = Frame(window, bg=bknd.dark_mode["background"])
frm_bottom.pack(padx=10)
background_element.append(frm_bottom)

btn_randomize = Button(frm_bottom, text="RANDOMIZE", font=button_font, width=12, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"], command=randomize)
btn_randomize.pack(side=LEFT, padx=10)
widget_element.append(btn_randomize)

btn_pack = Button(frm_bottom, text="PACK", font=button_font, width=12, bg=bknd.dark_mode["widget"], fg=bknd.dark_mode["text"])
btn_pack.pack(side=RIGHT, padx=10)
widget_element.append(btn_pack)