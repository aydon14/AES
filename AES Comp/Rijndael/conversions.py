# Conversions between bytes and hex / strings / Base64

# String -> Bytes
string = "000"
byte_string = string.encode('utf-8')

# Bytes -> String
byte_string = b"\x30\x30\x30" # or b"000"
string = byte_string.decode('utf-8')

# Bytes -> Hex
byte_string = b"\x30\x30\x30" # or b"000"
hex_string = byte_string.hex()

# Hex -> Bytes
hex_string = "303030"
byte_string = bytes.fromhex(hex_string)

# USE ME FOR BASE64 CONVERSIONS
base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Bytes -> Base64
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

byte_string = b"\x30\x30\x30" # or b"000"
base64_string = base64_encode(byte_string)

# Base64 -> Bytes
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

base64_string = "MDAw"
byte_string = base64_decode(base64_string)

# Bytes -> Base64 (Easier but Slower)
import base64

byte_string = b"\x30\x30\x30" # or b"000"
base64_string = base64.b64encode(byte_string)

# Base64 -> Bytes (Easier but Slower)
import base64

base64_string = "MDAw"
byte_string = base64.b64decode(base64_string)