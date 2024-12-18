from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP  # Импортируем шифратор для RSA


def encrypt(public_key, plaintext):
    """Шифрование сообщения с использованием открытого ключа"""
    rsa_public_key = RSA.import_key(public_key)  # Импортируем открытый ключ
    cipher = PKCS1_OAEP.new(rsa_public_key)  # Создаем объект шифрования
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))  # Шифруем сообщение
    return ciphertext  # Возвращаем зашифрованное сообщение

text = 'Hello Vladimir!!!'
pulic_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC95kajxtbaGNWwagRF8dZW4Vy8\nyfxTDiyyChAho0koQ2M4U14aFFdupN63Y+YWJRbWvD8E5wn4E1HKTD+7Q1dmmZKO\nM/BXJaDO0EVbyW3h8RioOCD1R/Qt/8fsCGhBhYI28zTRTgGfyRKvwQwwxblrumGt\nJEjn7AB/pCH1QhPQmQIDAQAB\n-----END PUBLIC KEY-----'
print(encrypt(pulic_key, text))