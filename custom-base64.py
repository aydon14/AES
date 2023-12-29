""" Using these functions might be faster than importing the built-in Base64 module. """

# Rijndael and other ciphers return non-utf-8 
# as ciphertext, so it has to be displayed as hex 
# or base64, which gives these functions a purpose.

# Both Functions use this string, do not delete!
base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Takes bytes (b'') and returns Base64 string ('') 
def base64_encode(byte_string):
    output_text = ""
    bits = 0
    bits_count = 0

    for byte in byte_string:
        bits <<= 8
        bits += byte
        bits_count += 8

        while bits_count >= 6:
            index = (bits >> (bits_count - 6)) & 63
            output_text += base64_alphabet[index]
            bits_count -= 6
            bits &= (1 << bits_count) - 1

    if bits_count > 0:
        bits <<= 6 - bits_count
        index = bits & 63
        output_text += base64_alphabet[index]

    while len(output_text) % 4 != 0:
        output_text += "="

    return output_text

# Takes Base64 string ('') and returns bytes (b'')
def base64_decode(encoded_text):
    byte_string = bytearray()
    bits = 0
    bits_count = 0

    for char in encoded_text:
        if char == '=':
            break

        index = base64_alphabet.index(char)
        bits = (bits << 6) + index
        bits_count += 6

        while bits_count >= 8:
            bits_count -= 8
            decoded_byte = (bits >> bits_count) & 0xFF
            byte_string.append(decoded_byte)

    return bytes(byte_string)