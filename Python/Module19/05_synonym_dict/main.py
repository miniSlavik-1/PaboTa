def sinonim(n):
    slovo = {}
    for i in range(n):
        print(i + 1, "пара:")
        a = input("")
        b = input("")
        slovo[a] = b
        slovo[b] = a
    return slovo

def search(slovo, text):
    if text in slovo:
        return "Синоним:", slovo[text]
    else:
        return "Такого слова в словаре нет."

n = int(input("Введите количество пар слов: "))
text = input("Введите слово: ")
print(search(sinonim(n), text))