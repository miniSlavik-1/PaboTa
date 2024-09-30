num = int(input("Кол-во чисел: "))
nummers = []
for i in range(num):
    nummers.append(int(input("Число: ")))

if nummers == nummers.reverse():
    print("Последовательность симметрична")

else:
    pass