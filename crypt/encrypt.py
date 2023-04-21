def encrypt(plain_text):
    encrypted_text = ""
    for char in plain_text:
        encrypted_text += str(ord(char)) + " "
    return encrypted_text.strip()

plain_text = input("Enter text to encrypt: ")
encrypted_text = encrypt(plain_text)

print("Encrypted Text: ", encrypted_text)
