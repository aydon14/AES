# Made by Aydon Fauscett

S_BOX = [
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

INV_S_BOX = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
]

RCON = [
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f
]

base64_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def key_expansion(key):
    key_size = len(key)
    key_words = [key[i:i + 4] for i in range(0, len(key), 4)]
    expanded_keys = list(key_words)
    if key_size == 16:
        Nr = 10
    elif key_size == 24:
        Nr = 12
    elif key_size == 32:
        Nr = 14

    Nk = key_size // 4

    for i in range(Nk, 4 * (Nr + 1)):
        temp = expanded_keys[i - 1]
        if key_size == 32 and i % Nk == 4:
            temp = [S_BOX[b] for b in temp]
        elif i % Nk == 0:
            temp = [temp[1], temp[2], temp[3], temp[0]]

            for j in range(4):
                temp[j] = S_BOX[temp[j]]

            temp[0] ^= RCON[i // Nk - 1]

        expanded_keys.append([a ^ b for a, b in zip(expanded_keys[i - Nk], temp)])

    return expanded_keys

def sub_bytes(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = S_BOX[state[i][j]]
    
    return state

def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = INV_S_BOX[state[i][j]]

    return state

def shift_rows(state):
    for i in range(4):
        state[0][i], state[1][i], state[2][i], state[3][i] = (
            state[(0 + i) % 4][i],
            state[(1 + i) % 4][i],
            state[(2 + i) % 4][i],
            state[(3 + i) % 4][i],
        )
    
    return state

def inv_shift_rows(state):
    for i in range(4):
        state[0][i], state[1][i], state[2][i], state[3][i] = (
            state[(0 - i) % 4][i],
            state[(1 - i) % 4][i],
            state[(2 - i) % 4][i],
            state[(3 - i) % 4][i],
        )
    
    return state

def mix_columns(state):
    for i in range(4):
        s = [state[i][j] for j in range(4)]

        state[i][0] = mul(0x02, s[0]) ^ mul(0x03, s[1]) ^ s[2] ^ s[3]
        state[i][1] = s[0] ^ mul(0x02, s[1]) ^ mul(0x03, s[2]) ^ s[3]
        state[i][2] = s[0] ^ s[1] ^ mul(0x02, s[2]) ^ mul(0x03, s[3])
        state[i][3] = mul(0x03, s[0]) ^ s[1] ^ s[2] ^ mul(0x02, s[3])

    return state

def inv_mix_columns(state):
    for i in range(4):
        s0 = state[i][0]
        s1 = state[i][1]
        s2 = state[i][2]
        s3 = state[i][3]

        state[i][0] = (
            (mul(0x0e, s0) ^ mul(0x0b, s1) ^ mul(0x0d, s2) ^ mul(0x09, s3))
        ) & 0xFF
        state[i][1] = (
            (mul(0x09, s0) ^ mul(0x0e, s1) ^ mul(0x0b, s2) ^ mul(0x0d, s3))
        ) & 0xFF
        state[i][2] = (
            (mul(0x0d, s0) ^ mul(0x09, s1) ^ mul(0x0e, s2) ^ mul(0x0b, s3))
        ) & 0xFF
        state[i][3] = (
            (mul(0x0b, s0) ^ mul(0x0d, s1) ^ mul(0x09, s2) ^ mul(0x0e, s3))
        ) & 0xFF

    return state

def mul(a, b):
    p = 0
    
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xFF
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
        
    return p

def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]

    return state

def inv_add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]

    return state

def pad(data, block_size):
    pad_len = block_size - len(data) % block_size
    padding = bytes([pad_len]) * pad_len
    return data + padding

def unpad(padded_data):
    pad_len = padded_data[-1]
    if pad_len < len(padded_data):
        return padded_data[:-pad_len]
    else:
        return padded_data

def base64_encode_bytes(byte_string):
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

def base64_decode_text(encoded_text):
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

def encrypt_block(block, key, key_size):
    if key_size == 16:
        Nr = 10
    elif key_size == 24:
        Nr = 12
    elif key_size == 32:
        Nr = 14

    state = block[:]
    state = add_round_key(state, key[:4])

    for round in range(1, Nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key[4 * round: 4 * round + 4])
    
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key[4 * Nr: 4 * Nr + 4])

    return state

def decrypt_block(block, key, key_size):
    if key_size == 16:
        Nr = 10
    elif key_size == 24:
        Nr = 12
    elif key_size == 32:
        Nr = 14

    state = block[:]
    state = add_round_key(state, key[4 * Nr: 4 * Nr + 4])

    for round in range(Nr - 1, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, key[4 * round: 4 * round + 4])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, key[:4])
    return state

def aes_encrypt(plaintext, key):
    key_size = len(key)
    expanded_key = key_expansion(key)
    block_size = 16
    ciphertext = b''
    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]

    for block in blocks:
        if len(block) < block_size:
            block = pad(block, block_size)

        state = [list(block[i:i+4]) for i in range(0, len(block), 4)]
        state = encrypt_block(state, expanded_key, key_size)
        encrypted_block = bytes(sum(state, []))
        ciphertext += encrypted_block

    return ciphertext

def aes_decrypt(ciphertext, key):
    key_size = len(key)
    expanded_key = key_expansion(key)
    block_size = 16
    plaintext = b''
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]

    for block in blocks:
        state = [list(block[i:i+4]) for i in range(0, len(block), 4)]
        state = decrypt_block(state, expanded_key, key_size)
        decrypted_block = bytes(sum(state, []))
        plaintext += decrypted_block

    plaintext = unpad(plaintext)
    return plaintext

def encode():
    plaintext_string = "0000000000000000"
    plaintext_bytes = plaintext_string.encode('utf-8')
    
    key_string = "00000000000000000000000000000000"
    key_bytes = key_string.encode('utf-8')
    
    ciphertext = aes_encrypt(plaintext_bytes, key_bytes)
    ciphertext = base64_encode_bytes(ciphertext)
    
    print(f"Original string: {plaintext_string}")
    print(f"Original bytes: {plaintext_bytes}")
    print(f"Encoded string: {ciphertext}")
    
    ciphertext = base64_decode_text(ciphertext)
    decrypted_plaintext = aes_decrypt(ciphertext, key_bytes)
    
    print(f"Decoded string: {decrypted_plaintext.decode('utf-8')}")
    
if __name__ == "__main__":
    encode()