def spisok(dlin: int):
    mass = []
    for char in range(dlin):
        if char % 2 == 0:
            mass.append(1)
        else:
            mass.append(char % 5)
    return mass


dlin = int(input("Введите длину списка: "))
print("Результат:", spisok(dlin))