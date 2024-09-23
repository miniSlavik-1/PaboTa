# Я честно говоря не очень понял, в чем смысл задачи и почему программа решила что 9 - четное число
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
for i in range(len(numbers_list)):
    t = 0
    for j in range(0, len(numbers_list) - 1):
        if numbers_list[j + 1] < numbers_list[j]:
            t = numbers_list[j + 1]
            numbers_list[j + 1] = numbers_list[j]
            numbers_list[j] = t
            t = 0

for k in numbers_list:
    if k % 2 == 1:
        numbers_list.remove(k)

print(numbers_list)