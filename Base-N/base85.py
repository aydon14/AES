# ascii85 with modified alphabet as defined in RFC 1924 (IPv6)
# https://www.dcode.fr/ascii-85-encoding

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"

def encrypt(input):
    data = input.encode('utf-8')
    result = ""
    data_len = len(data)

    i = 0
    while i < data_len:
        chunk = data[i:i+4]
        i += 4

        value = 0
        for j, byte in enumerate(chunk):
            value |= byte << (8 * (3 - j))

        encoded = ""
        for _ in range(5):
            encoded = alphabet[value % 85] + encoded
            value //= 85

        result += encoded

    if data_len % 4 != 0:
        result = result[:-(4 - data_len % 4)]

    return result

def decrypt(encoded_input):
    data_len = len(encoded_input)
    result = bytearray()

    i = 0
    while i < data_len:
        chunk = encoded_input[i:i+5]
        i += 5

        if 'u' in chunk:
            chunk = chunk.replace('u', '!')

        value = 0
        for j, char in enumerate(chunk):
            index = alphabet.index(char)
            value = value * 85 + index

        decoded = bytearray()
        for _ in range(4):
            decoded.insert(0, (value & 0xFF))
            value >>= 8

        result += decoded

    if data_len % 5 != 0:
        result = result[:-(5 - data_len % 5)]

    if result and result[-1] == 0x00:
        result[-1] = ord('!')

    return result.decode('utf-8')
