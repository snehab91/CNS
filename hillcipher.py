import numpy as np

def text_to_matrix(text, n):
    # Convert the input text to a matrix of numbers (A=0, B=1, ..., Z=25)
    matrix = []
    for char in text:
        if char.isalpha():
            matrix.append(ord(char.upper()) - ord('A'))
    # Pad the matrix with zeros if needed
    while len(matrix) % n != 0:
        matrix.append(0)
    return np.array(matrix).reshape(-1, n)

def matrix_to_text(matrix):
    # Convert a matrix of numbers back to text
    return ''.join(chr(int(x) % 26 + ord('A')) for x in matrix.flatten())

def encrypt_hill_cipher(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext_matrix = text_to_matrix(plaintext, n)
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    return matrix_to_text(ciphertext_matrix)

def decrypt_hill_cipher(ciphertext, key_matrix):
    n = len(key_matrix)
    key_matrix_inv = np.linalg.inv(key_matrix)  # Calculate the inverse of the key matrix
    ciphertext_matrix = text_to_matrix(ciphertext, n)
    plaintext_matrix = np.dot(ciphertext_matrix, key_matrix_inv) % 26
    return matrix_to_text(plaintext_matrix)

# Example usage
plaintext = "HELLO"
key_matrix = np.array([[6, 24], [13, 16]])  # Example key matrix

# Encrypt the plaintext using Hill cipher
ciphertext = encrypt_hill_cipher(plaintext, key_matrix)
print(f'Encrypted Text: {ciphertext}')

# Decrypt the ciphertext using Hill cipher
decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)
print(f'Decrypted Text: {decrypted_text}')