ALL files have purposes. Testing files are labeled so. Do your own research on modes. I will provide brief discriptions in the future.

P.S. You can delete the "encode()" function when using.

File format: cipher-mode.

Errors are not built in, so if your key is an invalid length for example, then you will recieve a regular python error.

Files only contain byte format. Check conversions.py for hex and regular string formats. File only contains examples, not import code.

I plan on adding all round 1 ciphers onto this repository.

--- Ciphers / Modes ---

-- Rijndael --

- Electronic Codebook (ECB)
- Cipher Block Chaining (CBC)
- Cipher Feedback (CFB)
- Output Feedback (OFB)
- Counter (CTR)
- Galois/Counter Mode (GCM) (upcoming)
- XEX Tweaked Codebook (XTS-AES) (upcoming)

All tests performed with Cryptography (https://github.com/pyca/cryptography/)

This may be vulnerable to side channel attacks. Learn more: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#Security
 ____________________________
/\/ \/ \/ \/ \__/ \/ \/ \/ \/\
\/\ Made by Aydon Fauscett /\/
 \/________________________\/