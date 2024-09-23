sdvig = int(input("Сдвиг: "))
tablo = [1, 2, 3, 4, 5]
print("Изначальный список:", tablo)
for i in range(sdvig):
    tablo.append(tablo[0])
    tablo.pop(0)
print("Сдвинутый список:", tablo)