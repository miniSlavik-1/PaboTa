array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
new_mass = []
new_mass_1 = []
for i in array_1:
    if i in array_2:
        if i in array_3:
            new_mass.append(i)
    if i not in array_2:
        if i not in array_3:
            new_mass_1.append(i)

print(new_mass)
print(new_mass_1)