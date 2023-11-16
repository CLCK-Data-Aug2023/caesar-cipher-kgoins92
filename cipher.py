abc = "abcdefghijklmnopqrstuvwxyz"
shift = int(input("Please enter the number of places to shift: "))
message = input("Please enter a sentence: ").lower()
encrypt_text = ""
for char in message:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
    encrypt_text += char
print(encrypt_text)