from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad


key = b"qwertyrw"
schifer = b"\x0e\xd0\xf6\x835\xb0N\xd7\x8dm\xcb0eFn\x12"
obj_encr = DES.new(key, DES.MODE_ECB)
result = obj_encr.decrypt(schifer)
result = unpad(result, 8)
print(result)