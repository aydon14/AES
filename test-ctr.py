from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b"0000000000000000"
plaintext = b"0000000000000000"

backend = default_backend()
counter = b"0000000000000000"

cipher = Cipher(algorithms.AES(key), modes.CTR(counter), backend=backend)
encryptor = cipher.encryptor()

ciphertext = encryptor.update(plaintext) + encryptor.finalize()

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext.hex())
print("Key:", key)