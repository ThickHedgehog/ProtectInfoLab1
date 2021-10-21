from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(raw, key, iv):
    data_bytes = bytes(raw, 'utf-8')
    padded_bytes = pad(data_bytes, AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted = cipher.encrypt(padded_bytes)
    return encrypted


def decrypt(raw, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted = cipher.decrypt(raw)
    extracted_bytes = unpad(decrypted, AES.block_size)
    return extracted_bytes
