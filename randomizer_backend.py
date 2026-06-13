"""
Program name : randomizer_backend.py
Author : Chokapi
Date : 08.04.2025
Modif : 13.06.2026
Version : 2.0
"""
import json
import os

import yaz0

base_path = "mod-file"
generator_folder = "generator"

##-----path handler-----##
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


##-----program-----##
generator_path = get_folder(base_path, generator_folder)