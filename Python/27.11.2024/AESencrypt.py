from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b"qwertyrwasdfghjk"
schifer = b"`2T\x89\xa2`\xf3\xc8\x1cv&K?\x15\xa3\x98"
obj = AES.new(key, AES.MODE_ECB)

result = obj.decrypt(schifer)
result = unpad(result, 16)
print(result)