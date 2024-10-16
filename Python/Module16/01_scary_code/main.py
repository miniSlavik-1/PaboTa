a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t1 = a.count(5)
while 5 in a:
    a.remove(5)
a.extend(c)
t2 = a.count(3)

print(t1)
print(t2)
print(a)