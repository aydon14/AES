import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Replace with your own key and plaintext
key = b"Thats my Kung Fu"  # Provide a 128-bit (16-byte) key
plaintext = b"Two One Nine Two"

# Padding the plaintext
backend = default_backend()
block_size = algorithms.AES.block_size // 8  # Block size in bytes
padded_length = (len(plaintext) + block_size - 1) // block_size * block_size
padder = lambda x: x + (padded_length - len(x)) * bytes([padded_length - len(x)])
padded_plaintext = padder(plaintext)

# Encrypt the padded plaintext
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# Encode the ciphertext to base64
base64_encoded = base64.b64encode(ciphertext).decode('utf-8')

print("Plaintext:", plaintext.decode('utf-8'))
print("Ciphertext (Base64):", base64_encoded)
print("Key:", key.hex())
