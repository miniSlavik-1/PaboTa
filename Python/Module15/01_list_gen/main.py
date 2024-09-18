number = int(input("Введите число: "))
res = []
for n in range(1, number + 1, 2):
    res.append(n)

print("Список из нечётных чисел от одного до N: ", res)