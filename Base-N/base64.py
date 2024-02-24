alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encrypt(input):
    output_text = ""
    bits = 0
    bits_count = 0

    for char in input:
        bits <<= 8
        bits += ord(char)
        bits_count += 8

        while bits_count >= 6:
            index = (bits >> (bits_count - 6)) & 63
            output_text += alphabet[index]
            bits_count -= 6
            bits &= (1 << bits_count) - 1

    if bits_count > 0:
        bits <<= 6 - bits_count
        index = bits & 63
        output_text += alphabet[index]

    while len(output_text) % 4 != 0:
        output_text += "="

    return output_text

def decrypt(input):
    output_text = ""
    bits = 0
    bits_count = 0

    for char in input:
        if char == "=":
            break

        index = alphabet.index(char)
        bits <<= 6
        bits += index
        bits_count += 6

        while bits_count >= 8:
            byte = (bits >> (bits_count - 8)) & 255
            output_text += chr(byte)
            bits_count -= 8
            bits &= (1 << bits_count) - 1

    return output_text
