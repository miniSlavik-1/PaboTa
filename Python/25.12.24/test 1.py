class User:
    name = "Admin"
    password = "qwerty"
    active = True


user_1 = User()
print(type(user_1))

print(user_1.name)

user_2 = User()
user_2.name = "Nimda"
print(user_2.name)