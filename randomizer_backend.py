"""
Program name : randomizer_backend.py
Author : Chokapi
Date : 08.04.2025
Modif : 11.04.2025
Version : 2.0
"""
#import
import os
import random

#path
mod_file = "mod-file"
gen_file = "mod-file/Pikmin3randomizer/Romfs/CMCmn/generator/mapB/plant.txt"

#-----object list-----
#enemies
enemies_list = ['"Amembo"', '"Arikui"', '"Awadako"', '"Billy"', '"Buriko"', '"Chappy"', '"TentenChappy"', '"CrystalFrog"',
                '"Damagumo"', '"Damagumo_Gold"', '"Egg"', '"Frog"', '"Futakuchi"', '"YukiFutakuchi"', '"HageDamagumo"',
                '"HageDamagumo_Gold"', '"Hambo"', '"Hiba"', '"Iwakko"', '"Jelly"', '"Kaburi"', '"Kajiokoshi"', '"Kanitama"',
                '"Karehambo"', '"Kawasumi"', '"Kemekuji"', '"KingChappy"', '"Kochappy"', '"TenKochappy"', '"Kogane"',
                '"Kokagami"', '"KokagamiEgg"', '"KumaChappy"', '"KumaKochappy"', '"Net"', '"Mar"', '"Mure"', '"Mush"',
                '"Namazu"', '"Otama"', '"Pelplant1"', '"Pelplant5"', '"Pelplant10"', '"Sarai"', '"Shako"', '"YellowShijimi"',
                '"RedShijimi"', '"WhiteShijimi"', '"SnakeCrow"', '"WaterTank"', '"FireTank"', '"BubbleTank"', '"TobiKaburi"',
                '"Tobinko"', '"Tobiuo"', '"UjinkoA"', '"UjinkoB"', '"UjinkoC"', '"Yamma"', '"MaroFrog"']

enemies_to_replace = ['"enemies"']

#fruits
fruits_list = ['"Apple"', '"Apricot"', '"Avocado"', '"Banana"', '"Cherry"', '"Dekopon"', '"Fig"', '"Gfruit"', '"Grape"',
               '"Kiwi"', '"KiwiGold"', '"Lemon"', '"Lime"', '"Loquat"', '"Mango"', '"Mangosteen"', '"Melon"', '"Mikan"',
               '"Muscat"', '"Nashi"', '"Papaya"', '"Peach"', '"Pear"', '"Persimmon"', '"Pitaya"', '"Plum"', '"Raspberry"',
               '"StarFruit"', '"Strawberry"', '"WaterMelon"']

fruits_to_replace = ['"fruits"']

#fruits
plants_list = ['"bell"', '"clover"', '"cosmos"', '"dongurinome"', '"dongurinome_aki"', '"erigeron"', '"hangesyou"',
               '"hikarikinoko"', '"himeturusoba"', '"ikariso"', '"inunohuguri"', '"katabami"', '"ooinu"', '"pansy"',
               '"rose"', '"sugar"', '"suisen"', '"tamokinoko"', '"tanpopo"', '"tanpopo_hana"', '"tanpopo_watage"',
               '"toubana"', '"turu_head"', '"turu_leaf"', '"urikawa"']

plants_to_replace = ['"plants"']

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


def randomize_file(path, replace, object_list):
    try:
        #read the gen file
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        new_lines = []
        #read each lign
        for line in lines:
            #split word in the lign
            words = line.split()
            for i in range(len(words)):
                #look if the word need to replace
                if words[i] in replace:
                    #chose a random element to replace with
                    words[i] = random.choice(object_list)
            new_lines.append(' '.join(words))
        #replace with the new data
        with open(path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
        print(f"Edited file: {path}")
    except UnicodeDecodeError as e:
        print(f"Error reading {path}: {e}")
    except Exception as e:
        print(f"An error occurred with file {path}: {e}")