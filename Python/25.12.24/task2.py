class User:
    name = "Admin"
    password = "qwerty"
    active = True

    def __str__(self):
        return f'Имя: {self.name}, \nпароль: {self.password}, \nактивность: {self.active}\n'



user_1 = User()
print(user_1)
