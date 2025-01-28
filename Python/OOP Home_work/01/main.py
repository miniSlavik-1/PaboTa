class Student:
    def __init__(self, FI, GN, oc):
        self.FI = FI
        self.group = GN
        self.oc = sum(oc) / len(oc)

    def __str__(self):
        return f"Name - {self.FI}, Group - {self.group}, Rang - {self.oc}"


stud1 = Student("Vl Chg", 31, [3, 5, 5, 3, 4])
print(stud1)
stud2 = Student("Cr Vr", 31, [5, 5, 3, 3, 2])
print(stud2)
stud3 = Student("Zv Mk", 31, [5, 5, 5, 4, 4])
print(stud3)
stud4 = Student("Al Nk", 31, [5, 3, 3, 3, 5])
print(stud4)
stud5 = Student("Kl Nk", 31, [5, 5, 5, 5, 5])
print(stud5)