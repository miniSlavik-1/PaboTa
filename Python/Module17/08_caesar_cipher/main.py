def shifer(stroka: str, key: int):
    alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    new_stroka = ""
    for i in range(len(stroka)):
        if stroka[i] in alp:
            ind = (alp.index(stroka[i]) + key) % len(alp)
            new_stroka += alp[ind]
        else:
            new_stroka += stroka[i]
    return new_stroka


strok = input("Введите сообщение: ")
key = int(input("Введите сдвиг: "))
print("Зашифрованное сообщение:", shifer(strok, key))