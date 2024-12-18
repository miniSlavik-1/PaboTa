p1 = 3011
p2 = 919

open_key = p1 * p2
print("Открытый ключ:", open_key)

Fn = (p1 - 1) * (p2 - 1)
e = 27631
print("Вторая часть открытого ключа:", e)

for d in range(10000000):
    if (d * e) % Fn == 1:
        print("Закрытый ключ:", d)


ck = 1677177
print(1677177 ** 3833911 % open_key)