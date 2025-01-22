class Potato:
    stad = {0: "Клубень", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, num):
        self.num = num
        self.state = 0

    def info(self):
        print(f"Картошка {self.num} на стадии {self.stad[self.state]}")

    def rost(self):
        if self.state <= 2:
            self.state += 1
        # self.info()

class Plant:
    def __init__(self, nums):
        self.potatos = [Potato(x) for x in range(1, nums + 1)]

    def rost_all(self):
        print("\nКартошка растет")
        for i in self.potatos:
            i.rost()

    def plant_info(self):
        print("\nСостояние грядки:")
        for i in self.potatos:
            i.info()

plant_1 = Plant(5)
plant_1.plant_info()
plant_1.rost_all()
plant_1.plant_info()