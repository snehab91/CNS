def rc4(key, plaintext):
    S = list(range(256))
    j = 0

    # Key-scheduling algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm (PRGA)
    i = j = 0
    ciphertext = []

    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        ciphertext.append(chr(ord(char) ^ k))

    return ''.join(ciphertext)

# Example usage
key = "SecretKey"
plaintext = "Hello, RC4!"
encrypted_text = rc4(key, plaintext)
print("Original Text:", plaintext)
print("Encrypted Text:", encrypted_text)

decrypted_text = rc4(key, encrypted_text)
print("Decrypted Text:", decrypted_text)