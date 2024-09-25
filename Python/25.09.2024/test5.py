

def Secret(open_sms: str, key: int) -> str:
    closed_sms = ""
    for i in open_sms:
        ind = ord(i) + key
        if i.isupper():
            if ind > 90:
                ind -= 26
        else:
            if ind > 122:
                ind -= 26
        closed_sms += chr(ind)
    return closed_sms


vop = int(input("1 - зашифровать, 2 - расшифровать: "))
sms = input("Введите сообщение: ")
key = int(input("Введите ключ: "))

if vop == 1:
    print(Secret(sms, key))
elif vop == 2:
    print(Secret(sms, 0 - key))