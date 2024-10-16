def Lisst(array1: list, array2: list):
    array1.extend(array2)
    array1.sort()
    lisst = set(array1)
    return list(lisst)


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

lisst = Lisst(list1, list2)



print(lisst)