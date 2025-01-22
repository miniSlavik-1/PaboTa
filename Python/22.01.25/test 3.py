class Tieren:
    logs = 4
    hvost = True

    def __str__(self):
        tale = "да" if self.hvost else "нет"
        return f"Всего ног - {self.logs}, Хвост - {tale}"

    def progul(self):
        print("Гуляет")


class Katze(Tieren):
    def sound(self):
        print("МЯУ")


class Hund(Tieren):
    def sound(self):
        print("ГАВ")

class Frog(Tieren):
    hvost = False

    def sound(self):
        print("КВА")

    def progul(self):
        print("Плывет")

dog1 = Hund()
cat1 = Katze()
frog1 = Frog()
print(dog1)
print(cat1)
print(frog1)
dog1.sound()
cat1.sound()
frog1.sound()
dog1.progul()
cat1.progul()
frog1.progul()