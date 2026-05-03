from customtkinter import *

default_font = ("TkDefaultFont", 20, "bold")
button_font = ("TkDefaultFont", 30, "bold")

class RandoCheckbox:
    def __init__(self, root, text, font, command=None):
        self.root = root
        self.text = text
        self.font = font
        if command is not None:
            self.command = command
        else:
            self.command = lambda: None
        self.var = StringVar(value="off")
        self.checkbox = CTkCheckBox(self.root, text=self.text, font=self.font, command=self.command,
                                             variable=self.var, onvalue="on", offvalue="off")


    def pack(self):
        self.checkbox.pack()


    def grid(self, row, column):
        self.checkbox.grid(row=row, column=column, sticky="w", pady=(10,0))


    def get_value(self):
        return self.var.get()


window = CTk()
window.title("Pikmin 3 Randomizer")

#finding the screen with and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#size of the window
sizex = 500
sizey = 330

#finding the middle of the screen
posx = screen_width // 2 - (sizex // 2)
posy = screen_height // 2 - (sizey // 2)

#place the window in the middle
window.geometry(f"{sizex}x{sizey}+{posx}+{posy}")

#make the window not resizable
window.resizable(False, False)

#----- top element -----
frm_top = CTkFrame(window, fg_color="transparent")  # transparent if you want background to show
frm_top.pack(side="top", fill="x", padx=10, pady=(10, 0))

frm_top.grid_columnconfigure(0, weight=1)
frm_top.grid_columnconfigure(1, weight=64)
frm_top.grid_columnconfigure(2, weight=1)
frm_top.grid_columnconfigure(3, weight=1)

button_info = CTkButton(frm_top, text="ℹ", font=button_font, width=50, height=50)
button_info.grid(row=0, column=0)

button_folder = CTkButton(frm_top, text="📁", font=button_font, width=50, height=50)
button_folder.grid(row=0, column=2)

button_option = CTkButton(frm_top, text="⛭", font=button_font, width=50, height=50)
button_option.grid(row=0, column=3)

#----- param -----
frm_param = CTkFrame(window, fg_color="transparent")  # transparent if you want background to show
frm_param.pack(side="top", fill="x", padx=10, pady=(0, 10))

frm_param.grid_columnconfigure(0, weight=1)
frm_param.grid_columnconfigure(1, weight=1)

#----- Left Side -----
cbx_enemies = RandoCheckbox(frm_param, "Randomize enemies", default_font)
cbx_enemies.grid(1, 0)

cbx_fruits = RandoCheckbox(frm_param, "Randomize fruits", default_font)
cbx_fruits.grid(2, 0)

cbx_musics = RandoCheckbox(frm_param, "Randomize musics", default_font)
cbx_musics.grid(3, 0)

cbx_spice = RandoCheckbox(frm_param, "True Spice Mode", default_font)
cbx_spice.grid(4, 0)

cbx_chaos = RandoCheckbox(frm_param, "Chaos Randomizer", default_font)
cbx_chaos.grid(5, 0)

#----- Right Side -----
cbx_nbgen = RandoCheckbox(frm_param, "Max Gen Num", default_font)
cbx_nbgen.grid(1, 1)

ent_nbgen = CTkEntry(frm_param, font=default_font, width=60, justify="center")
ent_nbgen.grid(row=1, column=1, sticky="e", pady=(10,0))

cbx_open = RandoCheckbox(frm_param, "Open Progression", default_font)
cbx_open.grid(2, 1)

cbx_iron = RandoCheckbox(frm_param, "Iron-min", default_font)
cbx_iron.grid(3, 1)

ent_iron = CTkEntry(frm_param, font=default_font, width=60, justify="center")
ent_iron.grid(row=3, column=1, sticky="e", pady=(10,0))

cbx_onion = RandoCheckbox(frm_param, "Randomize onions", default_font)
cbx_onion.grid(4, 1)

lbl_start_onion = CTkLabel(frm_param, text="First onion", font=default_font)
lbl_start_onion.grid(row=5, column=1, sticky="w", pady=(10,0))

onion_options = ["Random", "Red", "Rock", "Yellow", "Winged", "Blue"]

drp_start_onion = CTkOptionMenu(frm_param, font=default_font, values=onion_options, width=120)
drp_start_onion.set("Random")  # Default text
drp_start_onion.grid(row=5, column=1, sticky="e", pady=(10,0))

#----- bottom element -----
frm_bottom = CTkFrame(window, fg_color="transparent")  # transparent if you want background to show
frm_bottom.pack(side="top", fill="x", padx=10, pady=(10, 0))

frm_bottom.grid_columnconfigure(1, weight=1)
frm_bottom.grid_columnconfigure(2, weight=1)

button_folder = CTkButton(frm_bottom, text="Randomize", font=button_font, width=220, height=50)
button_folder.grid(row=0, column=1)

button_option = CTkButton(frm_bottom, text="Pack", font=button_font, width=220, height=50)
button_option.grid(row=0, column=2)

window.mainloop()