def block32(x): return [x + i for i in range(32)]


mtf_dictionary = block32(0x60) + block32(0x40) + \
    block32(0x20) + block32(0x00) + list(range(128, 256))


def mtf(data: bytes) -> bytes:
    dictionary = mtf_dictionary.copy()
    compressed = bytearray()
    rank = 0

    for c in data:
        rank = dictionary.index(c)
        compressed.append(rank)
        dictionary.pop(rank)
        dictionary.insert(0, c)

    return bytes(compressed)


def imtf(code: bytes) -> bytes:
    compressed = code
    dictionary = mtf_dictionary.copy()
    plain_text = bytearray()

    for rank in compressed:
        plain_text.append(dictionary[rank])
        e = dictionary.pop(rank)
        dictionary.insert(0, e)

    return bytes(plain_text)
