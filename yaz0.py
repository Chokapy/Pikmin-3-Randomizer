def yaz0_decompress(data: bytes) -> bytes:
    """Decompress Yaz0-compressed data (Nintendo format)."""
    if not data.startswith(b"Yaz0"):
        raise ValueError("Input is not Yaz0-compressed (missing header)")

    uncompressed_size = int.from_bytes(data[4:8], "big")  # target size
    src_offset = 16  # skip Yaz0 header
    dst = bytearray()
    valid_bit_count = 0
    code_byte = 0

    while src_offset < len(data) and len(dst) < uncompressed_size:
        if valid_bit_count == 0:
            if src_offset >= len(data):
                break
            code_byte = data[src_offset]
            src_offset += 1
            valid_bit_count = 8

        if (code_byte & 0x80) != 0:
            # Literal byte
            if src_offset >= len(data):
                break
            dst.append(data[src_offset])
            src_offset += 1
        else:
            # Compressed block
            if src_offset + 1 >= len(data):
                break
            byte1 = data[src_offset]
            byte2 = data[src_offset + 1]
            src_offset += 2

            dist = ((byte1 & 0xF) << 8) | byte2
            copy_src = len(dst) - (dist + 1)

            length = byte1 >> 4
            if length == 0:
                if src_offset >= len(data):
                    break
                length = data[src_offset] + 0x12
                src_offset += 1
            else:
                length += 2

            for _ in range(length):
                if copy_src < 0 or copy_src >= len(dst):
                    raise IndexError(
                        f"Invalid back-reference: copy_src={copy_src}, dst_len={len(dst)}"
                    )
                dst.append(dst[copy_src])
                copy_src += 1

        code_byte <<= 1
        valid_bit_count -= 1

    if len(dst) != uncompressed_size:
        print(
            f"⚠️ Warning: decompressed size {len(dst)} "
            f"!= expected {uncompressed_size}"
        )

    return bytes(dst)


def yaz0_compress(data: bytes) -> bytes:
    """Compress data using Yaz0 (simple implementation)."""
    import struct

    out = bytearray()
    out.extend(b'Yaz0')                        # Magic
    out.extend(struct.pack(">I", len(data)))   # Uncompressed size
    out.extend(b'\x00' * 8)                    # Padding / reserved

    src = 0
    valid_bits = 0
    code_byte = 0
    chunk = bytearray()

    while src < len(data):
        if valid_bits == 8:
            # Flush
            out.append(code_byte)
            out.extend(chunk)
            code_byte = 0
            chunk.clear()
            valid_bits = 0

        # For simplicity: no fancy pattern search, just store as literal
        code_byte = (code_byte << 1) | 1
        chunk.append(data[src])
        src += 1
        valid_bits += 1

    # Flush leftover
    code_byte <<= (8 - valid_bits)
    out.append(code_byte)
    out.extend(chunk)

    return bytes(out)


"""
data = yaz0_decompress(open("single.szs", "rb").read())

# save SARC
with open("MapUnit.sarc", "wb") as f:
    f.write(data)

# then parse SARC (requires a SARC parser)


# Take your raw file (e.g. decompressed SARC, JSON, etc.)
with open("MapUnit.sarc", "rb") as f:
    raw = f.read()

compressed = yaz0_compress(raw)

with open("example.szs", "wb") as f:
    f.write(compressed)
"""


