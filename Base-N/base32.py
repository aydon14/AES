alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

def encrypt(input):
    encoded_data = ""
    bits = 0
    bits_count = 0

    for char in input:
        bits <<= 8
        bits += ord(char)
        bits_count += 8

        while bits_count >= 5:
            index = (bits >> (bits_count - 5)) & 31
            encoded_data += alphabet[index]
            bits_count -= 5
            bits &= (1 << bits_count) - 1

    if bits_count > 0:
        bits <<= 5 - bits_count
        index = bits & 31
        encoded_data += alphabet[index]

    while len(encoded_data) % 8 != 0:
        encoded_data += "="

    return encoded_data

def decrypt(input):
    decoded_data = ""
    bits = 0
    bits_count = 0

    for char in input:
        if char == "=":
            break

        index = alphabet.index(char)
        bits <<= 5
        bits += index
        bits_count += 5

        while bits_count >= 8:
            byte = (bits >> (bits_count - 8)) & 255
            decoded_data += chr(byte)
            bits_count -= 8
            bits &= (1 << bits_count) - 1

    return decoded_data
