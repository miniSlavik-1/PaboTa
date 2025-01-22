class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return f"Name - {self.__name}, Age - {self.__age}"

    def get_count(self):
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(0, 121):
            self.__age = age
        else:
            raise Exception("Недопустимо")


class Student(Person):
    def __init__(self, name, age, univer):
        super().__init__(name, age)
        self.univer = univer

    def __str__(self):
        info = super().__str__()
        return f"{info}, Unik - {self.univer}"


class Trudyaga(Person):
    def __init__(self, name, age, work, zp):
        super().__init__(name, age)
        self.work = work
        self.zp = zp
        
    def __str__(self):
        info = super().__str__()
        return f"{info}, Pa6oTa - {self.work}, ZP - {self.zp}"


student1 = Student("Igor", 19, "MGU")
print(student1)

worker1 = Trudyaga("Stepan", 45, "Mosgaz", 48000)
print(worker1)