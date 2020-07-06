def rle(data: bytes, progress) -> bytes:
    code = bytearray()
    counter = 0
    last = data[0]

    def encode(data, cnt):
        code.append(data)
        code.append(cnt)

    for c in data:
        progress.next()
        if c == last:
            counter += 1
            if counter == 0xFF:
                encode(last, counter)
                counter = 0
        else:
            encode(last, counter)
            counter = 1
            last = c

    if counter > 0:
        encode(last, counter)
    return bytes(code)


def irle(code: bytes, progress) -> bytes:
    data = bytearray()

    def decode(data, cnt):
        return [data for tmp in range(cnt)]

    for i in range(0, len(code), 2):
        data.extend(decode(code[i], int(code[i+1])))
        progress.next(2)
    return bytes(data)
