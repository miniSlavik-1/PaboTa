from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# def generate_key(bits):
#     key = RSA.generate(bits)
#     private_key = key.export_key()
#     public_key = key.publickey().export_key()
#     return public_key, private_key


def encrypt(pub_key, text):
    obj = PKCS1_OAEP.new(RSA.import_key(pub_key))
    schifer = obj.encrypt(text.encode())
    return schifer


def decrypt(priv_key, schifr):
    obj = PKCS1_OAEP.new(RSA.import_key(priv_key))
    text = obj.decrypt(schifr)
    return text.decode()

pub = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC95kajxtbaGNWwagRF8dZW4Vy8\nyfxTDiyyChAho0koQ2M4U14aFFdupN63Y+YWJRbWvD8E5wn4E1HKTD+7Q1dmmZKO\nM/BXJaDO0EVbyW3h8RioOCD1R/Qt/8fsCGhBhYI28zTRTgGfyRKvwQwwxblrumGt\nJEjn7AB/pCH1QhPQmQIDAQAB\n-----END PUBLIC KEY-----'
priv = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC95kajxtbaGNWwagRF8dZW4Vy8yfxTDiyyChAho0koQ2M4U14a\nFFdupN63Y+YWJRbWvD8E5wn4E1HKTD+7Q1dmmZKOM/BXJaDO0EVbyW3h8RioOCD1\nR/Qt/8fsCGhBhYI28zTRTgGfyRKvwQwwxblrumGtJEjn7AB/pCH1QhPQmQIDAQAB\nAoGAS3cDg3o1T56m7OB0qkcc4pHUhMHQIEF1yZruJi/5lqKQ/4VB1CNZS4MBbueo\nPAypMtTERnJ6J7elvTrn6McuJ8u7/EDQJq8vx3PVj4whgSrm9YtJThJQtSZjHq6D\nc32dV0F4UIaSiql3b7YhYJ00wWDXKICPik8TG7iqVN2sTXECQQDIW7jDvlUJHWso\n/0/ZCPzCwAZ+y4imn9LZecBeoKGOvPUUfg1IN8Naat/kY8NnPOPFFKW7nkKrV+tF\ne8i3qYFzAkEA8qL/diDe2X2zl0LeMguDMkbbBxOr0W1yPP0+Ur93YJE7HnPnxhAm\nT5LYBlMKa16LmV61eQXBsXK5w3DD1itywwJASqG/5UoUqtyGejMALzwlyvV0de6i\n7E5EYDX17kmvZFgGgqehkvESl6+PzqdKtj38KgFS6tw8wU5ymONPFPrS+QJBAM4i\nyKIVXv6rmm4Bs0AVI8sNA3vJrIlqUEmcZNxsKgFyoSVIFzrf8YxdFwaYehup4TPV\nkJtW1q3o6AUwwlAr7X0CQQCZLvO0Biku32R76WlCUf98FLSqQAjlsxcGB2VQwb1q\naz1MyFUxk0xkKO2lGzmGlnmesA7arAbCd66LUyrWrFPY\n-----END RSA PRIVATE KEY-----'

# pub, priv = generate_key(1024)
text = input("Введите сообщение для шифрования: ")

TEXT = encrypt(pub, text)
print(TEXT.hex())
print(decrypt(priv, b'\x16?\x16)\xd2\x08\xc4\x9b\x11\xf7\xf1\xf5\x12\xa0^e\xae\xcc\xf9/[\xa6\xc8eB\xd1\xc4~\x06a\x91\xca\x87iXF\xb5\xb6\xc6\xc5^S4\x81\xca\x99\x1d\xee\x15\x9e,\x11\x06,M\xbbp\x0f\xbb\x9d\x0b)\xfd\xa2\xdd[\xa0\xee\xc9\xef\x9e\xe2\x9b\xba\x97\xbdl\xa8*\xe2;\xd9\xfb\x9b\x0c\\;\x86j\x8e`\x8b\x02\x15]~\xe3\xfa\x9bnb\xf1\xf1\xf9\xc9\x8b\xb3+\xcfe\xf8-\xa0\x89\x9b\xc8\xb1\x02C$`RZ\x98Y\x95\xa7\x1a'))