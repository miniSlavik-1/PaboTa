list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

lisst = list1 + list2
lisst.sort()
for i in lisst:
    t = lisst.count(i)
    for j in range(t - 1):
        lisst.remove(i)

print(lisst)