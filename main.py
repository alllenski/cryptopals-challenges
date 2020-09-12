from base64 import b64encode, b64decode

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(string):
    base64 = b64encode(bytes.fromhex(string)).decode()
    return base64


base64_string = hex_to_base64(hex_string)

print(base64_string)

print(b64decode(base64_string).decode('utf-8'))