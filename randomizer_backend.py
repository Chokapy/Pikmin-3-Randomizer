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
#from yaz0 import yaz0

#path
mod_folder = "mod-file"
gen_folder = "mod-file/Pikmin3randomizer/Romfs/CMCmn/generator"
music_folder = "mod-file/Pikmin3randomizer/Romfs/CMCmn/audio/audiores/stream"

#-----object list-----
#enemies
enemies_list = ['"Amembo"', '"Arikui"', '"Awadako"', '"Billy"', '"Buriko"', '"Chappy"', '"TentenChappy"', '"CrystalFrog"',
                '"Damagumo"', '"Damagumo_Gold"', '"Egg"', '"Frog"', '"Futakuchi"', '"YukiFutakuchi"', '"HageDamagumo"',
                '"HageDamagumo_Gold"', '"Hambo"', '"Hiba"', '"Iwakko"', '"Jelly"', '"Kaburi"', '"Kajiokoshi"', '"Kanitama"',
                '"Karehambo"', '"Kawasumi"', '"Kemekuji"', '"KingChappy"', '"Kochappy"', '"TenKochappy"', '"Kogane"',
                '"Kokagami"', '"KokagamiEgg"', '"KumaChappy"', '"KumaKochappy"', '"Net"', '"Mar"', '"Mure"', '"Mush"',
                '"Namazu"', '"Otama"', '"Pelplant1"', '"Pelplant5"', '"Pelplant10"', '"Sarai"', '"Shako"', '"YellowShijimi"',
                '"RedShijimi"', '"WhiteShijimi"', '"SnakeCrow"', '"WaterTank"', '"FireTank"', '"BubbleTank"', '"TobiKaburi"',
                '"Tobinko"', '"Tobiuo"', '"Tsuyukusa"', '"UjinkoA"', '"UjinkoB"', '"UjinkoC"', '"Yamma"', '"MaroFrog"']

enemies_to_replace = ['"Amembo"', '"Arikui"', '"Awadako"', '"Billy"', '"Buriko"', '"Chappy"', '"TentenChappy"', '"CrystalFrog"',
                '"Damagumo"', '"Damagumo_Gold"', '"Demejako"', '"Egg"', '"Frog"', '"Futakuchi"', '"YukiFutakuchi"', '"HageDamagumo"',
                '"HageDamagumo_Gold"', '"Hambo"', '"Hiba"', '"Iwakko"', '"Jelly"', '"Kaburi"', '"Kajiokoshi"', '"Kanitama"',
                '"Karehambo"', '"Kawasumi"', '"Kemekuji"', '"KingChappy"', '"Kochappy"', '"TenKochappy"', '"Kogane"',
                '"Kokagami"', '"KokagamiEgg"', '"KumaChappy"', '"KumaKochappy"', '"Net"', '"Mar"', '"Mure"', '"Mush"',
                '"Namazu"', '"Otama"', '"Pelplant1"', '"Pelplant5"', '"Pelplant10"', '"Sarai"', '"Shako"', '"YellowShijimi"',
                '"RedShijimi"', '"WhiteShijimi"', '"SnakeCrow"', '"WaterTank"', '"FireTank"', '"BubbleTank"', '"TobiKaburi"',
                '"Tobinko"', '"Tobiuo"', '"Tsuyukusa"', '"UjinkoA"', '"UjinkoB"', '"UjinkoC"', '"Yamma"', '"MaroFrog"']

#enemies drop
enemies_drop_list = ['"Amembo"#drop', '"Arikui"#drop', '"Awadako"#drop', '"Billy"#drop', '"Buriko"#drop', '"Chappy"#drop',
                     '"TentenChappy"#drop', '"CrystalFrog"#drop', '"Damagumo"#drop', '"Damagumo_Gold"#drop', '"Egg"#drop',
                     '"Frog"#drop', '"Futakuchi"#drop', '"YukiFutakuchi"#drop', '"HageDamagumo"#drop', '"HageDamagumo_Gold"#drop',
                     '"Hambo"#drop', '"Iwakko"#drop', '"Jelly"#drop', '"Kaburi"#drop', '"Kajiokoshi"#drop', '"Kanitama"#drop',
                     '"Karehambo"#drop', '"Kawasumi"#drop', '"Kemekuji"#drop', '"KingChappy"#drop', '"Kochappy"#drop',
                     '"TenKochappy"#drop', '"Kokagami"#drop', '"KokagamiEgg"#drop', '"KumaChappy"#drop', '"KumaKochappy"#drop',
                     '"Net"#drop', '"Mar"#drop', '"Mure"#drop', '"Mush"#drop', '"Namazu"#drop', '"Otama"#drop', '"Pelplant1"#drop',
                     '"Pelplant5"#drop', '"Pelplant10"#drop', '"Sarai"#drop', '"Shako"#drop', '"YellowShijimi"#drop', '"RedShijimi"#drop',
                     '"WhiteShijimi"#drop', '"SnakeCrow"#drop', '"WaterTank"#drop', '"FireTank"#drop', '"BubbleTank"#drop',
                     '"TobiKaburi"#drop', '"Tobinko"#drop', '"Tobiuo"#drop', '"UjinkoA"#drop', '"UjinkoB"#drop', '"UjinkoC"#drop',
                     '"MaroFrog"#drop']

enemies_drop_to_replace = ['"Amembo"#drop', '"Arikui"#drop', '"Awadako"#drop', '"Billy"#drop', '"Buriko"#drop', '"Chappy"#drop',
                           '"TentenChappy"#drop', '"CrystalFrog"#drop', '"Damagumo"#drop', '"Damagumo_Gold"#drop', '"Demejako"#drop',
                           '"Egg"#drop', '"Frog"#drop', '"Futakuchi"#drop', '"YukiFutakuchi"#drop', '"HageDamagumo"#drop',
                           '"HageDamagumo_Gold"#drop', '"Hambo"#drop', '"Iwakko"#drop', '"Jelly"#drop', '"Kaburi"#drop',
                           '"Kajiokoshi"#drop', '"Kanitama"#drop', '"Karehambo"#drop', '"Kawasumi"#drop', '"Kemekuji"#drop',
                           '"KingChappy"#drop', '"Kochappy"#drop', '"TenKochappy"#drop', '"Kokagami"#drop', '"KokagamiEgg"#drop',
                           '"KumaChappy"#drop', '"KumaKochappy"#drop', '"Net"#drop', '"Mar"#drop', '"Mure"#drop', '"Mush"#drop',
                           '"Namazu"#drop', '"Otama"#drop', '"Pelplant1"#drop', '"Pelplant5"#drop', '"Pelplant10"#drop',
                           '"Sarai"#drop', '"Shako"#drop', '"YellowShijimi"#drop', '"Tobinko"#drop', '"Tobiuo"#drop', '"UjinkoA"#drop',
                           '"UjinkoB"#drop', '"UjinkoC"#drop', '"MaroFrog"#drop']

#fruits
fruits_list = ['"Apple"', '"Apricot"', '"Avocado"', '"Banana"', '"Cherry"', '"Dekopon"', '"Fig"', '"Gfruit"', '"Grape"',
               '"Kiwi"', '"KiwiGold"', '"Lemon"', '"Lime"', '"Loquat"', '"Mango"', '"Mangosteen"', '"Melon"', '"Mikan"',
               '"Muscat"', '"Nashi"', '"Papaya"', '"Peach"', '"Pear"', '"Persimmon"', '"Pitaya"', '"Plum"', '"Raspberry"',
               '"StarFruit"', '"Strawberry"', '"WaterMelon"']

fruits_to_replace = ['"Apple"', '"Apricot"', '"Avocado"', '"Banana"', '"Cherry"', '"Dekopon"', '"Fig"', '"Gfruit"', '"Grape"',
               '"Kiwi"', '"KiwiGold"', '"Lemon"', '"Lime"', '"Loquat"', '"Mango"', '"Mangosteen"', '"Mikan"',
               '"Muscat"', '"Nashi"', '"Papaya"', '"Peach"', '"Pear"', '"Persimmon"', '"Pitaya"', '"Plum"', '"Raspberry"',
               '"StarFruit"', '"Strawberry"', '"WaterMelon"']

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
    os.startfile(mod_folder)


def randomize_file(path, replace, object_list):
    try:
        #read the gen file
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
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


def randomize_all(generator_folder, replace, object_list):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if text file
            if name.endswith('.txt'):
                file_path = os.path.join(path, name)
                #randomize the file
                randomize_file(file_path, replace, object_list)


def randomize_all_file_name(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    original_names = [os.path.splitext(f)[0] for f in files]
    extensions = [os.path.splitext(f)[1] for f in files]

    # Shuffle the names
    shuffled_names = original_names[:]
    random.shuffle(shuffled_names)

    # Step 1: Rename to temporary names to avoid overwriting
    temp_names = []
    for i, f in enumerate(files):
        temp_name = f"__tempfile_{i}__{extensions[i]}"
        os.rename(os.path.join(folder_path, f), os.path.join(folder_path, temp_name))
        temp_names.append(temp_name)

    # Step 2: Rename temporary files to shuffled names
    for temp_file, new_base in zip(temp_names, shuffled_names):
        new_name = new_base + os.path.splitext(temp_file)[1]
        os.rename(os.path.join(folder_path, temp_file), os.path.join(folder_path, new_name))
        print(f"{temp_file} → {new_name}")



"""
def decompress_szs(path):
    with open(path, "rb") as infile:
        yaz_obj = yaz0(inputobj=infile, compress=False)
        output = yaz_obj.decompress()
        with open(f"{path}.txt", "wb") as outfile:
            outfile.write(output.getvalue())


def decompress_genfile(generator_folder):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if text file
            if name.endswith('.szs'):
                file_path = os.path.join(path, name)
                #decompress the file
                decompress_szs(file_path)


def compress_szs(path):
    with open(path, "rb") as infile:
        yaz_obj = yaz0(inputobj=infile, compress=True)
        output = yaz_obj.compress()
        with open(f"{path}.szs", "wb") as outfile:
            outfile.write(output.getvalue())


def compress_genfile(generator_folder):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if text file
            if name.endswith('.txt'):
                file_path = os.path.join(path, name)
                #decompress the file
                compress_szs(file_path)
"""