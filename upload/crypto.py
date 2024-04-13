from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode



def pad_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data


def unpad_data(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data)
    return unpadded_data


def encrypt_data(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_plaintext = pad_data(plaintext)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return b64encode(ciphertext)


def decrypt_data(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    ciphertext = b64decode(ciphertext)
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    plaintext = unpad_data(padded_plaintext)
    return plaintext