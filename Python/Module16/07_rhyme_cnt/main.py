mans = [x+1 for x in range(int(input("Кол-во человек: ")))]
death_num = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", str(death_num) + "-й человек")

print("Текущий круг людей:", mans)
print("Начало счёта с номера", 1)

while len(mans) > 1:
    print("Выбывает человек под номером", mans[death_num % len(mans) - 1])
    mans.pop(death_num % len(mans) - 1)
    print()
    print("Текущий круг людей:", mans)
    print("Начало счёта с номера", death_num%len(mans) + 1)

print("Остался человек под номером", mans)