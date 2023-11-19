def prepare_text(text):
    # Convert the text to uppercase and remove spaces
    text = text.upper().replace(" ", "")
    # Replace 'J' with 'I' (Playfair cipher typically uses a 5x5 grid excluding 'J')
    text = text.replace("J", "I")
    return text

def generate_key_matrix(key):
    # Generate a 5x5 matrix for the Playfair cipher key
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = prepare_text(key)
    key_matrix = []

    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_positions(matrix, char):
    # Find the row and column indices of a character in the matrix
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_playfair(plaintext, key):
    plaintext = prepare_text(plaintext)
    key_matrix = generate_key_matrix(key)

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]

        row1, col1 = find_positions(key_matrix, char1)
        row2, col2 = find_positions(key_matrix, char2)

        if row1 == row2:
            # Same row, shift column indices
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column, shift row indices
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            # Form a rectangle, swap column indices
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return ciphertext

def decrypt_playfair(ciphertext, key):
    key_matrix = generate_key_matrix(key)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find_positions(key_matrix, char1)
        row2, col2 = find_positions(key_matrix, char2)

        if row1 == row2:
            # Same row, shift column indices
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column, shift row indices
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:
            # Form a rectangle, swap column indices
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]

    return plaintext

# Example usage
plaintext = "HELLO WORLD"
key = "KEYWORD"

# Encrypt the plaintext using Playfair cipher
ciphertext = encrypt_playfair(plaintext, key)
print(f'Encrypted Text: {ciphertext}')

# Decrypt the ciphertext using Playfair cipher
decrypted_text = decrypt_playfair(ciphertext, key)
print(f'Decrypted Text: {decrypted_text}')