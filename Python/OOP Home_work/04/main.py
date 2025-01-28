class Property:
    def __init__(self, worth):
        self.worth = worth

    def nalog(self):
        nalogi = self.worth * 0.001
        return nalogi

    def __str__(self):
        return self.nalog()

class Apartment(Property):
    def nalog(self):
        nalogi = self.worth * 0.001
        return nalogi


class Car(Property):
    def nalog(self):
        nalogi = self.worth * (1/200)
        return nalogi


class CountryHouse(Property):
    def nalog(self):
        nalogi = self.worth * 0.002
        return nalogi

h = int(input("Сколько у вас денег? "))
a = input("Есть ли у вас квартира? (да/нет) ")
if a == "да":
    p1 = int(input("Какова её стоимость? "))
    n1 = Apartment(p1).__str__()
else:
    n1 = 0.0

b = input("Есть ли у вас машина? (да/нет) ")
if b == "да":
    p2 = int(input("Какова её стоимость? "))
    n2 = Car(p2).__str__()
else:
    n2 = 0.0

c = input("Есть ли у вас дача? (да/нет) ")
if c == "да":
    p3 = int(input("Какова её стоимость? "))
    n3 = CountryHouse(p3).__str__()
else:
    n3 = 0.0

sum = n1 + n2 + n3
if h < sum:
    print(f"Для оплаты налогов вам нехватает {sum - h}")
else:
    print(f"Налоги могут быть оплачены, останется {h - sum}")
