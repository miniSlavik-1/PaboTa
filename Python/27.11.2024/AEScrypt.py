from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


key = b"qwertyrwasdfghjk"
data = pad(b"Hello World", 16)
obj = AES.new(key, AES.MODE_ECB)

result = obj.encrypt(data)

print(result)
print(result.hex())