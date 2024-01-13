from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b"0000000000000000"
plaintext = b"0000000000000000"
iv = b"1111111111111111"

backend = default_backend()
block_size = algorithms.AES.block_size // 8
padded_length = (len(plaintext) + block_size - 1) // block_size * block_size
padder = lambda x: x + (padded_length - len(x)) * bytes([padded_length - len(x)])
padded_plaintext = padder(plaintext)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext.hex())
print("Key:", key)
