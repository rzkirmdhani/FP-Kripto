import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import numpy as np

# Generate chaos keys (Tent Map)
def generate_tent_key(length):
    x = 0.5
    key = []
    for _ in range(length):
        x = 2 * x if x < 0.5 else 2 * (1 - x)
        key.append(int(x * 255))
    return bytes(key)

# Generate chaos keys (Logistic Map)
def generate_logistic_key(length, r=3.9, x0=0.5):
    x = x0
    key = []
    for _ in range(length):
        x = r * x * (1 - x)
        key.append(int(x * 255))
    return bytes(key)

# AES Encryption with Tent Map
def encrypt_with_tent_map(file_path, output_folder):
    with open(file_path, 'rb') as f:
        data = f.read()

    key = generate_tent_key(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    output_path = os.path.join(output_folder, "tent_encrypted_" + os.path.basename(file_path))
    with open(output_path, 'wb') as f:
        f.write(cipher.iv + ciphertext)

    return output_path

# AES Encryption with Logistic Map
def encrypt_with_logistic_map(file_path, output_folder):
    with open(file_path, 'rb') as f:
        data = f.read()

    key = generate_logistic_key(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    output_path = os.path.join(output_folder, "logistic_encrypted_" + os.path.basename(file_path))
    with open(output_path, 'wb') as f:
        f.write(cipher.iv + ciphertext)

    return output_path

# AES Decryption
def decrypt_file(file_path, output_folder):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Assuming Logistic Map key for decryption (adjust as needed)
    key = generate_logistic_key(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    output_path = os.path.join(output_folder, "decrypted_" + os.path.basename(file_path).replace("encrypted_", ""))
    with open(output_path, 'wb') as f:
        f.write(plaintext)

    return output_path
