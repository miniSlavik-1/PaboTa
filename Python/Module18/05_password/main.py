parol = input("Придумайте пароль: ")
if len(parol) >= 8:
    for i in range(1000):
        if str(i)[-1:0:-1] in parol or str(i) in parol:
            for j in range(len(parol)):
                if parol[j] in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    print("Это надёжный пароль!")
                    break
else:
    print("Пароль ненадёжный. Попробуйте ещё раз")