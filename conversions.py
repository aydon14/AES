# Conversions between bytes and hex / strings

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
