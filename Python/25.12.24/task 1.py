class Unit:
    def __init__(self, name):
        self.name = name
        self.damage = 20
        self.helth = 100

    def attack(self, name):
        name.helth -= self.damage
        print(f"{self.name} атаковал, у {name.name} осталось {name.helth}\n")

    def info(self):
        print(f"Имя: {self.name}, Здоровье: {self.helth}, Урон: {self.damage}")

unit_1 = Unit("Pavel")
unit_2 = Unit("Nikita")
unit_1.attack(unit_2)

unit_1.info()
unit_2.info()
