def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            
            # Shift the character by the specified amount
            shifted_char = chr((ord(char) + shift))

            result += shifted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
shift_amount = int(input("enter shift value "))

# Encrypt the plaintext using Caesar cipher
encrypted_text = caesar_cipher(plaintext, shift_amount)
print(f'Encrypted Text: {encrypted_text}')

# Decrypt the ciphertext (with a negative shift to reverse the encryption)
decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print(f'Decrypted Text: {decrypted_text}')