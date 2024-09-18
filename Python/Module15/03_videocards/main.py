num = int(input("Количество видеокарт: "))
nvidia = []
for n in range(num):
    nvidia.append(int(input(str(n + 1) + " Видеокарта: ")))

print("Старый список видеокарт:", nvidia)
newvidia = []
for elem in nvidia:
    if elem < max(nvidia):
        newvidia.append(elem)
print("Новый список видеокарт:", newvidia)
