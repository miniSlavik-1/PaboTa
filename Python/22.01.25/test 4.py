class Plav_sredstvo:
    def __init__(self, model, komand, name):
        self.__model = model
        self.__komand = komand
        self.__name = name

    def __str__(self):
        return f"Название - {self.__name}, Модель - {self.__model}, Экипаж - {self.__komand} человек"

    def get_name(self):
        return self.__name

    def marsh(self):
        print("Судно вышло на курс")


class Korabl(Plav_sredstvo):
    def __init__(self, model, komand, name, gun):
        super().__init__(model, komand, name)
        self.gun = gun

    def atack(self):
        print(f"Корабль {self.get_name()} атакует с помощью {self.gun}")


class Sudno(Plav_sredstvo):
    def __init__(self, model, komand, name):
        super().__init__(model, komand, name)
        self.kargo = 0

    def zagruz(self):
        if self.kargo < 5:
            self.kargo += 1
            print(f"Судно загружено на {self.kargo}")
        else:
            print("Перегруз")

    def razdruz(self):
        if self.kargo > 0:
            self.kargo -= 1
            print(f"Судно разгружено до {self.kargo}")
        else:
            print("Уже разгружено")


kor1 = Korabl("6П70", 60, "Стерегущий", "Москит")
print(kor1)
kor1.atack()
sudno1 = Sudno("Barkas", 30, "Париж")
print(sudno1)
sudno1.zagruz()
sudno1.zagruz()
sudno1.marsh()