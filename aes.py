from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

iv = get_random_bytes(AES.block_size)
def encrypt(text, key):
    text = text.encode('utf-8')
    key = key.encode('utf-8')
    #iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(text, AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    result = b64encode(iv + ciphertext).decode('utf-8')
    return result

def decrypt(ciphertext, key):
    key = key.encode('utf-8')
    ciphertext = b64decode(ciphertext.encode('utf-8'))
    #iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return decrypted_text.decode('utf-8')


plaintext = "Hello, AES!"
key = "ThisIsASecretKey"


encrypted_text = encrypt(plaintext, key)
print(f'Encrypted Text: {encrypted_text}')


decrypted_text = decrypt(encrypted_text, key)
print(f'Decrypted Text: {decrypted_text}')
