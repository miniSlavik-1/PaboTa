import random

sdvig = int(input("Сдвиг: "))

tablo = [random.randint(0,10) for i in range(5)]
print("Изначальный список:", tablo)

new_table = [tablo[(x + sdvig) % len(tablo)] for x in range(len(tablo))]
print("Сдвинутый список:", new_table)