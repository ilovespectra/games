def decrypt(encrypted_text):
    decrypted_text = ""
    encrypted_list = encrypted_text.split()
    for code in encrypted_list:
        decrypted_text += chr(int(code))
    return decrypted_text

encrypted_text = input("Enter encrypted text to decrypt: ")
decrypted_text = decrypt(encrypted_text)

print("Decrypted Text: ", decrypted_text)
