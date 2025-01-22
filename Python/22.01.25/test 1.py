class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child_list = []

    def __str__(self):
        return f"Имя - {self.name}, Возраст - {self.age}, Дети: {self.child_list}"

    def add_childs(self, num):
        if isinstance(num, Chado) and self.age - num.age >= 16:
            self.child_list.append(num.name)
        else:
            self.child_list.append(num)

    def uspokoit(self, child):
        if isinstance(child, Chado):
            child.bespokoystvo = False
            print("Успокоен")
        else:
            print("ErrOr")

    def prikorm(self, child):
        if isinstance(child, Chado):
            child.hunger = False
            print("Покормлен")
        else:
            print("ErrOr")


class Chado:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = False
        self.bespokoystvo = False

    def __str__(self):
        return f"Имя - {self.name}, Возраст - {self.age}, Состояние спокойствия - {self.bespokoystvo}, состояние голода - {self.hunger}"

    def golod(self):
        self.hunger = True
        print("Проголодался")

    def son(self):
        self.bespokoystvo = True
        print("Стал беспокойный")


parent1 = Parent("Igor", 37)
print(parent1)

child1 = Chado("Stas", 16)
print(child1)

parent1.add_childs(child1)
print(parent1)

child1.golod()
print(child1)
parent1.prikorm(child1)
print(child1)
