Here's the deal: I hate modules. Why import modules when you can save milliseconds of your time?

I was unable to find any pure python implementations of AES that strictly follow NIST FIPS 197:

https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf

So I decided to make my own. Current updates will be posted on this repository.

128, 192, and 256 bit versions are built-in each file.

There are no special errors, warnings, etc that I've implemented.

Each cipher takes and returns bytes. If you want base64 or hex, check conversions.py .

Sticking with the no modules theme, I made my own base64 functions for you to use, also in conversions.py .

--- Ciphers / Modes ---

-- Rijndael --

- Electronic Codebook (ECB)
- Cipher Block Chaining (CBC)
- Cipher Feedback (CFB)
- Output Feedback (OFB)
- Counter (CTR)
- Galois/Counter Mode (GCM)

--- --- --- --- --- ---

All tests performed with Cryptography (https://github.com/pyca/cryptography/)

This may be vulnerable to side channel attacks. Learn more: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#Security
_____________________________
Made by Aydon Fauscett

-- .- -.. . / -... -.-- / .- -.-- -.. --- -. / ..-. .- ..- ... -.-. . - -

01001101 01100001 01100100 01100101 00100000 01100010 01111001 00100000 01000001 01111001 01100100 01101111 01101110 00100000 01000110 01100001 01110101 01110011 01100011 01100101 01110100 01110100 

4d616465206279204179646f6e204661757363657474

TWFkZSBieSBBeWRvbiBGYXVzY2V0dA==

++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>+++++++.>---.+++.+.<<++.>>---.+++++++++++++++++++++++.<<.>------------.>.---------------------.+++++++++++.-.<<.>+++++.>-------------.++++++++++++++++++++.--.----------------.++.+++++++++++++++..
