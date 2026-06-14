"""
Program name : randomizer_backend.py
Author : Chokapi
Date : 08.04.2025
Modif : 13.06.2026
Version : 2.0
"""
import json
import os
import random
import re

import yaz0
import sarc

base_path = "mod-file"
generator_folder = "generator"
music_folder = "stream"

##-----path/file handler-----##
def get_list(path):
    """
    get_list allow to get json file
    :param path: path to a JSON file containing randomizer pool
    :return: the data of the JSON file
    """
    with open(path, 'r') as f:
        return json.load(f)


def get_folder(root_dir, target_folder):
    """
    get_folder allow to find a specific without knowing the path
    :param root_dir: root path to look in
    :param target_folder: folder to find
    :return: the folder path
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if target_folder in dirnames:
            return os.path.join(dirpath, target_folder)
    return None


##-----archive handler-----##
def unpack_all():
    """
    unpack_all unpack all .szs files to .sarc files
    """
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".szs"):
                file_path = os.path.join(dirpath, filename)

                ##-decompress file-##
                with open(file_path, 'rb') as f:
                    data = f.read()

                decompressed_data = yaz0.decompress(data)

                ##-write file-##
                # replace .szs with .sarc
                out_path = os.path.splitext(file_path)[0] + ".sarc"

                with open(out_path, "wb") as f:
                    f.write(decompressed_data)

                print(f"Decompressed {file_path} -> {out_path}")


def pack_all():
    """
    pack_all pack all .sarc files to .szs files
    """
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".sarc"):
                file_path = os.path.join(dirpath, filename)

                ##-compress file-##
                with open(file_path, 'rb') as f:
                    data = f.read()

                compressed_data = yaz0.compress(data)

                ##-write file-##
                # replace .sarc with .szs
                out_path = os.path.splitext(file_path)[0] + ".szs"

                with open(out_path, "wb") as f:
                    f.write(compressed_data)

                #delete base file
                os.remove(file_path)

                print(f"Compressed {file_path} -> {out_path} (removed original)")


##-----random function-----##
#random mean that any possible combination can be made
def randomize_objects(sarc_path, search_pool, random_pool, chance):
    """
    randomize_file randomize a .sarc file
    :param sarc_path: .sarc file path
    :param search_pool: objet that will be randomized
    :param random_pool: objet that will be randomized into
    """
    with open(sarc_path, "rb") as f:
        archive = sarc.read_file_and_make_sarc(f)

    writer = sarc.SARCWriter(be=False)

    count = 0

    for file_name in archive.list_files():
        data = bytes(archive.get_file_data(file_name)).splitlines(True)

        for i, line in enumerate(data):
            for search in search_pool:
                if f"\"{search}\"".encode() in line:
                    random_chance = random.uniform(0, 1)
                    if random_chance <= chance:
                        line = line.replace(
                            f"\"{search}\"".encode(),
                            f"\"{random.choice(random_pool)}\"".encode()
                        )
                        count += 1

            data[i] = line

        writer.add_file(file_name, b"".join(data))

    print(f"Replaced {count} occurrences")

    with open(sarc_path, "wb") as f:
        writer.write(f)


def randomize_all_objects(data_file_path, chance = 1.0):
    """
    randomize_all randomize all .sarc files
    :param data_file_path: the pool data
    """
    data = get_list(data_file_path)
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".sarc"):
                file_path = os.path.join(dirpath, filename)

                print(f"Randomizing : {file_path}")

                randomize_objects(file_path, data["search_pool"], data["random_pool"], chance)


def randomize_params(sarc_path, object, param_name, values, chance):
    object_found = False
    with open(sarc_path, "rb") as f:
        archive = sarc.read_file_and_make_sarc(f)

    writer = sarc.SARCWriter(be=False)

    count = 0

    for file_name in archive.list_files():
        data = bytes(archive.get_file_data(file_name)).splitlines(True)

        for i, line in enumerate(data):
            if f"\"{object}\"".encode() in line:
                object_found = True

            if object_found:
                if f"\"{param_name}\"".encode() in line:
                    if i + 1 < len(data):
                        random_chance = random.uniform(0, 1)
                        if random_chance <= chance:
                            data[i + 1] = re.sub(
                                rb"-?\d+(?:\.\d+)?",
                                lambda m: str(random.choice(values)).encode(),
                                data[i + 1],
                                count=1
                            )
                            count += 1


                    object_found = False

        writer.add_file(file_name, b"".join(data))

    print(f"Replaced {count} occurrences")

    with open(sarc_path, "wb") as f:
        writer.write(f)


def randomize_all_params(data_file_path, chance = 1.0):
    data = get_list(data_file_path)
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".sarc"):
                file_path = os.path.join(dirpath, filename)

                print(f"Randomizing : {file_path}")

                randomize_params(file_path, data["object"], data["param"], data["values"], chance)


##-----shuffle function-----##
#shufle mean that each element appear once
def shuffle_objects(sarc_path, search_pool, random_pool):
    with open(sarc_path, "rb") as f:
        archive = sarc.read_file_and_make_sarc(f)

    writer = sarc.SARCWriter(be=False)

    count = 0

    for file_name in archive.list_files():
        data = bytes(archive.get_file_data(file_name)).splitlines(True)

        for i, line in enumerate(data):
            for search in search_pool:
                if f"\"{search}\"".encode() in line:
                    replace = random.choice(random_pool)
                    line = line.replace(
                        f"\"{search}\"".encode(),
                        f"\"{replace}\"".encode()
                    )
                    print(i, line)
                    count += 1
                    random_pool.remove(replace)
                    break

            data[i] = line

        writer.add_file(file_name, b"".join(data))

    print(f"Replaced {count} occurrences")

    with open(sarc_path, "wb") as f:
        writer.write(f)

    return random_pool


def shuffle_all_objects(data_file_path):
    """
    randomize_all randomize all .sarc files
    :param data_file_path: the pool data
    """
    data = get_list(data_file_path)
    random_list = data["pool"].copy()
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".sarc"):
                file_path = os.path.join(dirpath, filename)

                print(f"Randomizing : {file_path}")

                print(random_list)
                new_pool = shuffle_objects(file_path, data["pool"], random_list)
                random_list = new_pool


def shuffle_params(sarc_path, param_name, values):
    #TODO being able the randomize a param
    pass


def shuffle_all_params(data_file_path):
    #TODO being able the randomize all params
    pass


def shuffle_files(dir):
    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    original_names = [os.path.splitext(f)[0] for f in files]
    extensions = [os.path.splitext(f)[1] for f in files]

    # Shuffle the names
    shuffled_names = original_names[:]
    random.shuffle(shuffled_names)

    # Rename to temporary names to avoid overwriting
    temp_names = []
    for i, f in enumerate(files):
        temp_name = f"__tempfile_{i}__{extensions[i]}"
        os.rename(os.path.join(dir, f), os.path.join(dir, temp_name))
        temp_names.append(temp_name)

    # Rename temporary files to shuffled names
    for temp_file, new_base in zip(temp_names, shuffled_names):
        new_name = new_base + os.path.splitext(temp_file)[1]
        os.rename(os.path.join(dir, temp_file), os.path.join(dir, new_name))
        print(f"{temp_file} → {new_name}")


##-----program-----##

generator_path = get_folder(base_path, generator_folder)
b = f"{generator_path}".encode()

unpack_all()

print("#-----Misc-----#")
randomize_all_params("data/randomizerData/Pongashi.json", 0.9)
shuffle_all_objects("data/randomizerData/Upgrades.json")

print("#-----Enemies-----#")
randomize_all_objects("data/randomizerData/Enemies.json")

print("#-----Fruits-----#")
randomize_all_objects("data/randomizerData/Fruits.json")

pack_all()

music_path = get_folder(base_path, music_folder)
shuffle_files(music_path)