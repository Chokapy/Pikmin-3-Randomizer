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
import struct
import re
import yaz0

#path
mod_folder = "mod-file"
gen_folder = "mod-file/Pikmin3randomizer/Romfs/CMCmn/generator"
music_folder = "mod-file/Pikmin3randomizer/Romfs/CMCmn/audio/audiores/stream"

#-----object list-----
#enemies
enemies_list = [
    b"Amembo", b"Arikui", b"Awadako", b"Billy", b"Buriko", b"Chappy", b"TentenChappy", b"CrystalFrog",
    b"Damagumo", b"Damagumo_Gold", b"Egg", b"Frog", b"Futakuchi", b"YukiFutakuchi", b"HageDamagumo",
    b"HageDamagumo_Gold", b"Hambo", b"Hiba", b"Iwakko", b"Jelly", b"Kaburi", b"Kajiokoshi", b"Kanitama",
    b"Karehambo", b"Kawasumi", b"Kemekuji", b"KingChappy", b"Kochappy", b"TenKochappy", b"Kogane",
    b"Kokagami", b"KokagamiEgg", b"KumaChappy", b"KumaKochappy", b"Net", b"Mar", b"Mure", b"Mush",
    b"Namazu", b"Otama", b"Pelplant1", b"Pelplant5", b"Pelplant10", b"Sarai", b"Shako", b"YellowShijimi",
    b"RedShijimi", b"WhiteShijimi", b"SnakeCrow", b"WaterTank", b"FireTank", b"BubbleTank", b"TobiKaburi",
    b"Tobinko", b"Tobiuo", b"Tsuyukusa", b"UjinkoA", b"UjinkoB", b"UjinkoC", b"MaroFrog"
]

# Enemies to replace
enemies_to_replace = [
    b"Amembo", b"Arikui", b"Awadako", b"Billy", b"Buriko", b"Chappy", b"TentenChappy", b"CrystalFrog",
    b"Damagumo", b"Damagumo_Gold", b"Demejako", b"Egg", b"Frog", b"Futakuchi", b"YukiFutakuchi", b"HageDamagumo",
    b"HageDamagumo_Gold", b"Hambo", b"Hiba", b"Iwakko", b"Jelly", b"Kaburi", b"Kajiokoshi", b"Kanitama",
    b"Karehambo", b"Kawasumi", b"Kemekuji", b"KingChappy", b"Kochappy", b"TenKochappy", b"Kogane",
    b"Kokagami", b"KokagamiEgg", b"KumaChappy", b"KumaKochappy", b"Net", b"Mar", b"Mure", b"Mush",
    b"Namazu", b"Otama", b"Pelplant1", b"Pelplant5", b"Pelplant10", b"Sarai", b"Shako", b"YellowShijimi",
    b"RedShijimi", b"WhiteShijimi", b"SnakeCrow", b"WaterTank", b"FireTank", b"BubbleTank", b"TobiKaburi",
    b"Tobinko", b"Tobiuo", b"Tsuyukusa", b"UjinkoA", b"UjinkoB", b"UjinkoC", b"Yamma", b"MaroFrog"
]

# Enemies drop
enemies_drop_list = [
    b"Amembo", b"Arikui", b"Awadako", b"Billy", b"Buriko", b"Chappy",
    b"TentenChappy", b"CrystalFrog", b"Damagumo", b"Damagumo_Gold", b"Egg",
    b"Frog", b"Futakuchi", b"YukiFutakuchi", b"HageDamagumo", b"HageDamagumo_Gold",
    b"Hambo", b"Iwakko", b"Jelly", b"Kaburi", b"Kajiokoshi", b"Kanitama",
    b"Karehambo", b"Kawasumi", b"Kemekuji", b"KingChappy", b"Kochappy",
    b"TenKochappy", b"Kokagami", b"KokagamiEgg", b"KumaChappy", b"KumaKochappy",
    b"Net", b"Mar", b"Mure", b"Mush", b"Namazu", b"Otama", b"Pelplant1",
    b"Pelplant5", b"Pelplant10", b"Sarai", b"Shako", b"YellowShijimi", b"RedShijimi",
    b"WhiteShijimi", b"SnakeCrow", b"WaterTank", b"FireTank", b"BubbleTank",
    b"TobiKaburi", b"Tobinko", b"Tobiuo", b"UjinkoA", b"UjinkoB", b"UjinkoC",
    b"MaroFrog"
]

enemies_drop_to_replace = [
    b"Amembo", b"Arikui", b"Awadako", b"Billy", b"Buriko", b"Chappy",
    b"TentenChappy", b"CrystalFrog", b"Damagumo", b"Damagumo_Gold", b"Egg",
    b"Frog", b"Futakuchi", b"YukiFutakuchi", b"HageDamagumo", b"HageDamagumo_Gold",
    b"Hambo", b"Iwakko", b"Jelly", b"Kaburi", b"Kajiokoshi", b"Kanitama",
    b"Karehambo", b"Kawasumi", b"Kemekuji", b"KingChappy", b"Kochappy",
    b"TenKochappy", b"Kokagami", b"KokagamiEgg", b"KumaChappy", b"KumaKochappy",
    b"Net", b"Mar", b"Mure", b"Mush", b"Namazu", b"Otama", b"Pelplant1",
    b"Pelplant5", b"Pelplant10", b"Sarai", b"Shako", b"YellowShijimi", b"RedShijimi",
    b"WhiteShijimi", b"SnakeCrow", b"WaterTank", b"FireTank", b"BubbleTank",
    b"TobiKaburi", b"Tobinko", b"Tobiuo", b"UjinkoA", b"UjinkoB", b"UjinkoC",
    b"MaroFrog"
]

# Fruits
fruits_list = [
    b"Apple", b"Apricot", b"Avocado", b"Banana", b"Cherry", b"Dekopon", b"Fig", b"Gfruit",
    b"Kiwi", b"KiwiGold", b"Lemon", b"Lime", b"Loquat", b"Mango", b"Mangosteen", b"Melon", b"Mikan",
    b"Nashi", b"Papaya", b"Peach", b"Pear", b"Persimmon", b"Pitaya", b"Plum", b"Raspberry",
    b"StarFruit", b"Strawberry", b"WaterMelon"
]

fruits_to_replace = [
    b"Apple", b"Apricot", b"Avocado", b"Banana", b"Cherry", b"Dekopon", b"Fig", b"Gfruit", b"Grape",
    b"Kiwi", b"KiwiGold", b"Lemon", b"Lime", b"Loquat", b"Mango", b"Mangosteen", b"Mikan",
    b"Muscat", b"Nashi", b"Papaya", b"Peach", b"Pear", b"Persimmon", b"Pitaya", b"Plum", b"Raspberry",
    b"StarFruit", b"Strawberry", b"WaterMelon"
]

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


# --- helpers ---
def read_u16(d,o,be): return struct.unpack_from(">H" if be else "<H", d,o)[0]
def read_u32(d,o,be): return struct.unpack_from(">I" if be else "<I", d,o)[0]
def write_u32(buf,o,val,be): struct.pack_into(">I" if be else "<I", buf,o,val)


def parse_sarc(raw: bytes):
    assert raw[:4]==b"SARC","Not a SARC"
    be=(read_u16(raw,6,True)==0xFEFF)
    header_size=read_u16(raw,4,True)
    data_off=read_u32(raw,12,be)
    version=read_u16(raw,16,be)
    off_sfat=raw.find(b"SFAT",0,0x400)
    node_count=read_u16(raw,off_sfat+6,be)
    hash_key=read_u32(raw,off_sfat+8,be)
    sfat_header_size=read_u16(raw,off_sfat+4,be)
    nodes_off=off_sfat+sfat_header_size
    node_bytes,nodes=[],[]
    for i in range(node_count):
        o=nodes_off+0x10*i
        node_bytes.append(bytearray(raw[o:o+0x10]))
        start,end=read_u32(raw,o+8,be),read_u32(raw,o+12,be)
        nodes.append((start,end))
    off_sfnt=raw.find(b"SFNT",0,0x2000)
    sfnt_block=raw[off_sfnt:data_off]
    files=[bytearray(raw[data_off+s:data_off+e]) for s,e in nodes]
    return dict(be=be,header_size=header_size,data_off=data_off,
                version=version,hash_key=hash_key,
                node_bytes=node_bytes,files=files,sfnt_block=bytearray(sfnt_block))


def rebuild_sarc(meta,new_files):
    be=meta["be"]; new_data=bytearray(); new_nodes=[]
    for f in new_files:
        s=len(new_data); new_data+=f; e=len(new_data)
        pad=(4-(e&3))&3; new_data+=b"\x00"*pad; e+=pad
        new_nodes.append((s,e))
    out=bytearray(b"SARC")
    out+=struct.pack(">H",meta["header_size"])
    out+=struct.pack(">H",0xFEFF if be else 0xFFFE)
    out+=b"\x00\x00\x00\x00"
    sfat_header=bytearray(b"SFAT")
    sfat_header+=struct.pack(">H" if be else "<H",0x0C)
    sfat_header+=struct.pack(">H" if be else "<H",len(new_nodes))
    sfat_header+=struct.pack(">I" if be else "<I",meta["hash_key"])
    node_blob=bytearray()
    for i,node16 in enumerate(meta["node_bytes"]):
        s,e=new_nodes[i]
        write_u32(node16,8,s,be); write_u32(node16,12,e,be)
        node_blob+=node16
    sfat_block=sfat_header+node_blob
    sfnt_block=bytes(meta["sfnt_block"])
    data_off=0x14+len(sfat_block)+len(sfnt_block)
    out+=struct.pack(">I" if be else "<I",data_off)
    out+=struct.pack(">H" if be else "<H",meta["version"])
    out+=b"\x00\x00"
    out+=sfat_block+sfnt_block+new_data
    write_u32(out,8,len(out),be)
    return bytes(out)


def randomize_bytes(buf: bytearray, replace_list: list[bytes], pool: list[bytes], tag: str | None = None) -> bytearray:
    text = buf.decode("utf-8", errors="ignore")

    # Decode replace_list into strings
    replace_words = [w.decode() for w in replace_list]

    if tag:
        # Match only quoted words followed by the tag
        words_pattern = "|".join(re.escape(w) for w in replace_words)
        pattern = re.compile(r'"(' + words_pattern + r')"' + re.escape(tag))
    else:
        # Match only quoted words without a tag after
        words_pattern = "|".join(re.escape(w) for w in replace_words)
        pattern = re.compile(r'"(' + words_pattern + r')"(?!#)')

    def replacer(match):
        old = match.group(1).encode()
        candidates = [c for c in pool if c != old]
        if not candidates:
            return match.group(0)
        new = random.choice(candidates).decode()

        if tag:
            return f'"{new}"{tag}'
        else:
            return f'"{new}"'

    new_text = pattern.sub(replacer, text)
    return bytearray(new_text, "utf-8")


# --- main function ---
def randomize_file(path: str, replace_list: list[bytes], object_list: list[bytes], tag: str, out_path: str|None=None):
    """
    Randomize a SARC archive by replacing occurrences of bytes in replace_list
    with random choices from object_list. Works with variable-length replacements.

    :param path: Path to input .sarc file
    :param replace_list: List of byte strings to replace
    :param object_list: Pool of byte strings to pick from
    :param out_path: Optional output file path (defaults to overwriting `path`)
    :param tag: None
    :return: Bytes of the new randomized SARC
    """
    with open(path, "rb") as f:
        data = f.read()

    meta = parse_sarc(data)
    new_files = [randomize_bytes(f, replace_list, object_list, tag) for f in meta["files"]]
    rebuilt = rebuild_sarc(meta, new_files)

    # Default: overwrite the input file
    if out_path is None:
        out_path = path

    with open(out_path, "wb") as f:
        f.write(rebuilt)

    print(f"✅ Randomized SARC written to: {out_path}")
    return rebuilt


def randomize_all(generator_folder, replace, object_list, tag: str | None = None):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if text file
            if name.endswith('.sarc'):
                file_path = os.path.join(path, name)
                #randomize the file
                randomize_file(file_path, replace, object_list, tag)


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


def decompress_szs(path):
    print("Decompressing:", path)
    with open(path, "rb") as f:
        data = f.read()

    decompressed = yaz0.yaz0_decompress(data)

    # replace .szs with .sarc
    base, _ = os.path.splitext(path)
    out_path = base + ".sarc"

    with open(out_path, "wb") as f:
        f.write(decompressed)

    print(f"Saved decompressed SARC -> {out_path}")


def decompress_genfile(generator_folder):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if szs file
            if name.endswith('.szs'):
                file_path = os.path.join(path, name)
                #decompress the file
                decompress_szs(file_path)


def compress_szs(path):
    # Take your raw file (e.g. decompressed SARC, JSON, etc.)
    with open(path, "rb") as f:
        raw = f.read()

    # Prevent double-compression
    if raw.startswith(b"Yaz0"):
        raise ValueError(f"{path} already looks Yaz0-compressed!")

    compressed = yaz0.yaz0_compress(raw)

    # Replace .sarc with .szs
    base, _ = os.path.splitext(path)
    out_path = base + ".szs"

    with open(out_path, "wb") as f:
        f.write(compressed)

    # Optionally remove the old .sarc file
    os.remove(path)

    print(f"Compressed {path} -> {out_path} (removed original)")


def compress_genfile(generator_folder):
    for path, subdirs, files in os.walk(generator_folder):
        for name in files:
            #check if sarc file
            if name.endswith('.sarc'):
                file_path = os.path.join(path, name)
                #decompress the file
                compress_szs(file_path)