import struct

def decompress(data: bytes) -> bytes:
    if not data.startswith(b"Yaz0"):
        raise ValueError("Not Yaz0-compressed")
    uncompressed_size = int.from_bytes(data[4:8], "big")
    src, dst = 16, bytearray()
    valid_bit_count, code_byte = 0, 0
    while src < len(data) and len(dst) < uncompressed_size:
        if valid_bit_count == 0:
            code_byte = data[src]; src += 1
            valid_bit_count = 8
        if code_byte & 0x80:
            dst.append(data[src]); src += 1
        else:
            byte1, byte2 = data[src], data[src+1]; src += 2
            dist = ((byte1 & 0xF) << 8) | byte2
            copy_src = len(dst) - (dist + 1)
            length = (byte1 >> 4) + 2
            if length == 2:
                length = data[src] + 0x12; src += 1
            for _ in range(length):
                dst.append(dst[copy_src]); copy_src += 1
        code_byte <<= 1; valid_bit_count -= 1
    return bytes(dst)


def compress(data: bytes) -> bytes:
    out = bytearray()
    out.extend(b"Yaz0")
    out.extend(struct.pack(">I", len(data)))
    out.extend(b"\x00" * 8)
    src, valid_bits, code_byte, chunk = 0, 0, 0, bytearray()
    while src < len(data):
        if valid_bits == 8:
            out.append(code_byte); out.extend(chunk)
            code_byte, chunk, valid_bits = 0, bytearray(), 0
        code_byte = (code_byte << 1) | 1
        chunk.append(data[src]); src += 1; valid_bits += 1
    code_byte <<= (8 - valid_bits)
    out.append(code_byte); out.extend(chunk)
    return bytes(out)