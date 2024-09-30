Schlittschuhe = int(input("Кол-во коньков: "))
sizes = []
for i in range(Schlittschuhe):
    print("Размер ", str(i + 1) + "-й пары: ", end = " ")
    size = int(input(""))
    sizes.append(size)

Menschen = int(input("\nКол-во людей: "))
foots = []
for i in range(Menschen):
    print("Размер ноги", str(i + 1) + "-го человека: ", end = " ")
    size = int(input(""))
    foots.append(size)

dovolno = 0
for i in foots:
    if i in sizes:
        dovolno += 1
        sizes.remove(i)
        foots.remove(i)

print("Наибольшее кол-во людей, которые могут взять ролики:", dovolno)