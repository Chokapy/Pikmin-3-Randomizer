"""
Program name : randomizer_backend.py
Author : Chokapi
Date : 08.04.2025
Modif : 10.04.2025
Version : 2.0
"""
#import
import os

#path
mod_file = "mod-file"

#color pallet
dark_mode = {
    "text" : "#FFFFFF",
    "widget" : "#666666",
    "background" : "#1A1A1A"
}

light_mode = {
    "text" : "#000000",
    "widget" : "#D9CCDD",
    "background" : "#F0F0F0"
}

def open_mod_folder():
    os.startfile(mod_file)