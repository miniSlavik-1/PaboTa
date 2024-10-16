mans = [x+1 for x in range(int(input("Кол-во человек: ")))]
death_num = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", str(death_num) + "-й человек\n")

start = 0
for i in range(len(mans) - 1):
    print("\nТекущий круг людей:", mans)
    print("Начало счёта с номера", mans[start])
    in_rm = (death_num + start - 1 ) % len(mans)
    print("Выбывает человек под номером", mans[in_rm])
    mans.pop(in_rm)
    start = in_rm % len(mans)

print("Остался человек под номером", mans)