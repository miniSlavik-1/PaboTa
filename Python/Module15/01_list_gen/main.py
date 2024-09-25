number = int(input("Введите число: "))
res = [x for x in range(1, number + 1, 2)]
# for n in range(1, number + 1, 2):
#     res.append(n)

print("Список из нечётных чисел от одного до N: ", res)