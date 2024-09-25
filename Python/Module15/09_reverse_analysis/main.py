# Я честно говоря не очень понял, в чем смысл задачи и почему программа решила что 9 - четное число
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
for i in range(len(numbers_list) - 1, 0, -1):
    if numbers_list[i] % 2 == 0:
        print(numbers_list[i], end = " ")