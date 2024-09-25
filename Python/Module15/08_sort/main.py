import random


n = int(input())
mass = [random.randint(10, 20) for i in range(n)]
print(mass)

for j in range(len(mass) - 1):
    for i in range(0, len(mass) - 1):
        if mass[i] > mass[i + 1]:
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
print(mass)
