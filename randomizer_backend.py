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

import yaz0
import sarc

base_path = "mod-file"
generator_folder = "generator"

##-----path/file handler-----##
def get_list(path):
    with open(path, 'r') as f:
        return json.load(f)


def get_folder(root_dir, target_folder):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if target_folder in dirnames:
            return os.path.join(dirpath, target_folder)
    return None


##-----archive handler-----##
def unpack_all():
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
def randomize_file(sarc_path, search_pool, random_pool):
    with open(sarc_path, "rb") as f:
        archive = sarc.read_file_and_make_sarc(f)

    writer = sarc.SARCWriter(be=False)

    count = 0

    for file_name in archive.list_files():
        data = bytes(archive.get_file_data(file_name)).splitlines(True)

        for i, line in enumerate(data):
            for search in search_pool:
                if f"\"{search}\"".encode() in line:
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

def randomize_all(data_file_path):
    data = get_list(data_file_path)
    for dirpath, dirnames, filenames in os.walk(generator_path):
        for filename in filenames:

            if filename.endswith(".sarc"):
                file_path = os.path.join(dirpath, filename)

                randomize_file(file_path, data["search_pool"], data["random_pool"])


##-----program-----##

generator_path = get_folder(base_path, generator_folder)
b = f"{generator_path}".encode()

unpack_all()

randomize_all("data/randomizerData/Enemies.json")
randomize_all("data/randomizerData/Fruits.json")

pack_all()