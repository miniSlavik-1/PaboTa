import random

list1 = []
for i in range(4):
    list2 = []
    for j in range(3):
        list2.append(random.randint(0, 20))
    list1.append(list2)
print(list1)