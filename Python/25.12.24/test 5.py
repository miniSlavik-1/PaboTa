class Employer:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def info(self):
        print(f"Имя: {self.name},\nзарплата: {self.salary}\n")


emp_1 = Employer("1", 20000)
emp_1.info()

emp_2 = Employer("2", 30000)
emp_2.info()

emp_3 = Employer("4", 50000)
emp_3.info()