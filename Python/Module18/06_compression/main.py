stroka = input("Введите строку: ")
stor = ""
for i in range(len(stroka)):
    c = 1
    if stroka[i] == stroka[0]:
        c += 1
    stor += stroka[i] + str(c)
print(stor)