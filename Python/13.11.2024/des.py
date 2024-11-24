from encodings.utf_7 import encode

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

# Исходный текст
text = input("Введите сообщение: ").encode()
print("Исходный текст:", text) # Вывод в 16-ричном виде

# Генерация ключа
# key = os.urandom(8) # Генерируем 8 случайных байт (64 бит) ключа
key = input("").encode()
key = pad(key, 8)
print("KEY:", key.hex()) # Вывод в 16-ричном виде

# Шифрование
schifer = DES.new(key, DES.MODE_ECB) # Создаем объект шифрования в режиме ECB (режис СВС дополняется ИВ)
text = pad(text, 8) # Заполнение нулями исходного сообщения до 64 бит (8 байт)
result = schifer.encrypt(text) # Шифрование
print("Зашифрованный текст:", result) # Вывод в 16-ричном виде

# Раcшифрование
deschifer = DES.new(key, DES.MODE_ECB) # Создаем объект шифрования в режиме ECB (режис СВС дополняется ИВ)
result0 = deschifer.decrypt(result) #
result01 = unpad(result0, 8) # Удаляем незначащие нули
print("Расшифровано:", result01) #