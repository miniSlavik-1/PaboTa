import random

def sorevn(a, b):
    c = []
    for i in range(20):
        if a[i] > b[i]:
            c.append(a[i])
        elif a[i] < b[i]:
            c.append(b[i])
    return(c)

a = [random.randint(5, 10) for x in range(20)]
b = [random.randint(5, 10) for x in range(20)]

print("Первая команда:", a)
print("Вторая команда:", b)
print("Победители тура:", sorevn(a, b))