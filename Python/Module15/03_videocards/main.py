num = int(input("Количество видеокарт: "))
nvidia = [int(input(str(x + 1) + " Видеокарта: ")) for x in range(num)]
# for n in range(num):
#     nvidia.append(int(input(str(n + 1) + " Видеокарта: ")))

print("Старый список видеокарт:", nvidia)
newvidia = [x for x in nvidia if x < max(nvidia)]
# for elem in nvidia:
#     if elem < max(nvidia):
#         newvidia.append(elem)
print("Новый список видеокарт:", newvidia)
