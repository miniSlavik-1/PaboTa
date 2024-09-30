a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a += b
t1 = a.count(5)
for i in range(t1):
    a.remove(5)
a += c
t2 = a.count(3)

print(t1)
print(t2)
print(a)