mass = []
for i in range(10):
    if i % 2 == 0:
        mass.append(i)
print(mass)

mass1 = [x for x in range(10) if x % 2 == 0 ]
print(mass1)
