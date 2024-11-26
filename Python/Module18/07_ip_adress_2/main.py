ip = input("Введите IP: ")
ipp = ip.split(".")
for i in ipp:
    if int(i) or int(i) == 0:
        if int(i) > 255:
            print(i, "превышает 255")
            break
    else:
        print(i, "- это не целое число")
        break
else:
    print("IP-адрес корректен")
