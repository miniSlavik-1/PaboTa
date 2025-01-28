class Unit:
    def __init__(self, heatpoints):
        self.health = heatpoints

    def uron(self):
        self.health -= 0
        print("Получен урон")


class Soldier(Unit):
    def uron(self, uron):
        if self.health > uron:
            self.health -= uron
            print(f"Получен урон {uron}, осталось {self.health}")
        else:
            print("Уже умер")


class Mirniy(Unit):
    def uron(self, uron):
        if self.health > 2*uron:
            self.health -= 2 * uron
            print(f"Получен урон {uron * 2}, осталось {self.health}")
        else:
            print("Уже умер")

mir1 = Mirniy(2)
mir1.uron(5)
mir1.uron(1)