class Family:
    surname = "Ivanovy"
    money = 100000
    house = False

    def info(self):
        print(
            f"Фамилия: {self.surname},\n"
            f"Деньги: {self.money},\n"
            f"Дом: {self.house}\n"
        )

    def farming(self, zp):
        self.money += zp
        print(f"Вы заработали: {zp},\nИтого: {self.money}\n")

    def housing(self, price):
        if self.money >= price:
            self.money -= price
            self.house = True
            print(f"Поздравляю с покупкой дома за {price},\nосталось: {self.money}\n")
        else:
            print(f"Не хватает: {price - self.money}\n")

family = Family()
family.info()
family.housing(1000000)
for i in range(10):
    family.farming(10000)
family.housing(200000)
family.info()