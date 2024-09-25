mass = []
for i in range(10):
    if i % 2 == 0:
        mass.append(i)
    else:
        mass.append(1)
print(mass)

mass1 = [x if x % 2 == 0 else 1 for x in range(10)]
print(mass1)