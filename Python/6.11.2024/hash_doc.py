import hashlib


hash = hashlib.new('md5', b'privet').hexdigest()
print(hash)

text = "QwErTy123"
hash2 = hashlib.new("sha256", text.encode()).hexdigest()
print(hash2)