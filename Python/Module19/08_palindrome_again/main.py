a = input("Введите строку: ")
line = 0
for i in range(len(a)):
    if a.count(a[i]) % 2 != 0:
        line += 1
if line > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")