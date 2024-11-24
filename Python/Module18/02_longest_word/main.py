strok = input("Введите строку: ")
st = strok.split(" ")
m = len(st[0])
slovo = ""
for i in st:
    if len(i) > m:
        m = len(i)
        slovo = i

print("Самое длинное слово:", slovo)
print("Длина этого слова:", m)