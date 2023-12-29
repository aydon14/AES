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
_____________________________
Made by Aydon Fauscett
-- .- -.. . / -... -.-- / .- -.-- -.. --- -. / ..-. .- ..- ... -.-. . - -
01001101 01100001 01100100 01100101 00100000 01100010 01111001 00100000 01000001 01111001 01100100 01101111 01101110 00100000 01000110 01100001 01110101 01110011 01100011 01100101 01110100 01110100 
4d616465206279204179646f6e204661757363657474
TWFkZSBieSBBeWRvbiBGYXVzY2V0dA==
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++.>---.+++.+.<<++.>>---.+++++++++++++++++++++++.<<.>------------.>.---------------------.+++++++++++.-.<<.>+++++.>-------------.++++++++++++++++++++.--.----------------.++.+++++++++++++++..