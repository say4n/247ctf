import pytesseract
from PIL import Image

file = "my_magic_bytes.jpg.enc"

with open(file, "rb") as f:
    data = f.read()

signature = [0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01]

file_bytes = list(map(lambda x: int(x), data[:12]))

key = []

for i in range(12):
    key.append(signature[i] ^ file_bytes[i])

data = list(data)

for i in range(len(data)):
    data[i] = int(data[i]) ^ key[i % len(key)]

with open("my_magic_bytes.jpg", "wb") as f:
    f.write(bytearray(data))

text = pytesseract.image_to_string("my_magic_bytes.jpg")
print(text)

