import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = b"0000000000000000"  # Provide 16, 24, or 32 byte key
plaintext = b"0000000000000000"

backend = default_backend()
counter = b"0000000000000000"

cipher = Cipher(algorithms.AES(key), modes.CTR(counter), backend=backend)
encryptor = cipher.encryptor()

ciphertext = encryptor.update(plaintext) + encryptor.finalize()

base64_encoded = base64.b64encode(ciphertext).decode('utf-8')
hex_ciphertext = ciphertext.hex()

print("Plaintext:", plaintext.decode('utf-8'))
print("Ciphertext (Base64):", base64_encoded)
print("Ciphertext (Hex):", hex_ciphertext)
print("Key:", key.decode('utf-8'))
print("Key (Hex):", key.hex())