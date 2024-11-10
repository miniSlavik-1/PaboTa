def glas(text: str) -> list:
    stinng = "аоуеияэё"
    lisst = []
    for char in text:
        if char.lower() in stinng:
            lisst.append(char)

    return lisst


text = input("Введите текст: ")

print("Список гласных букв:", glas(text))
print("Длина списка:", len(glas(text)))