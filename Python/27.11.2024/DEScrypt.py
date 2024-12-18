from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


key = b"qwertyrw"
data = pad(b"Hello World", 8)

obj_crypto = DES.new(key, DES.MODE_ECB)
result = obj_crypto.encrypt(data)
print(result.hex())
print(result)