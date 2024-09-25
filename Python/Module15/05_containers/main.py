num = int(input("Количество контейнеров: "))
containers = [int(input("Введите вес контейнера: ")) for x in range(num)]
# for n in range(num):
#     cont = int(input("Введите вес контейнера: "))
#     containers.append(cont)

x = int(input("Введите вес нового контейнера: "))
c = 1
for i in containers:
    if x <= i:
        c += 1
print("Номер, который получит новый контейнер:", c)