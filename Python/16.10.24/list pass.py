a = open("password.txt", "w")

for i in range(10):
    a.write(str(i))

a.close()