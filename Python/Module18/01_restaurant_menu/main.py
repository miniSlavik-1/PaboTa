# def menu(lisst):
#     lisst = lisst.split(";")
#     print("На данный момент в меню есть:", end =" ")
#     for i in range(len(lisst) - 1):
#         print(lisst[i], end=", ")
#     print(lisst[-1])

meno = input("Доступное меню: ")
print(", ".join(meno.split(";")))