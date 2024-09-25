def Secret(open_sms: str, key: int) -> str:
    alpf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    closed_sms = ""
    for char in open_sms:
        if char in alpf:
            ind = alpf.index(char)
            closed_sms += alpf[(ind + key) % len(alpf)]
        else:
            closed_sms += char
    return closed_sms


vop = int(input("1 - зашифровать, 2 - расшифровать: "))
sms = input("Введите сообщение: ")
key = int(input("Введите ключ: "))

if vop == 1:
    print(Secret(sms, key))
elif vop == 2:
    print(Secret(sms, 0 - key))