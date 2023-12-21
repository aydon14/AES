import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b"0000000000000000"  # Provide 16, 24, or 32 byte key
plaintext = b"0000000000000000"
iv = b"1111111111111111"  # Initialization Vector (IV) - 16 bytes

backend = default_backend()
block_size = algorithms.AES.block_size // 8
padded_length = (len(plaintext) + block_size - 1) // block_size * block_size
padder = lambda x: x + (padded_length - len(x)) * bytes([padded_length - len(x)])
padded_plaintext = padder(plaintext)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

base64_encoded = base64.b64encode(ciphertext).decode('utf-8')
hex_ciphertext = ciphertext.hex()

print("Plaintext:", plaintext.decode('utf-8'))
print("Ciphertext (Base64):", base64_encoded)
print("Ciphertext (Hex):", hex_ciphertext)
print("Key:", key.decode('utf-8'))
print("Key (Hex):", key.hex())
