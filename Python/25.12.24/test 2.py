class User:
    name = "Admin"
    password = "qwerty"
    active = True

    def print_info(self):
        print(f'Имя: {self.name}, \nпароль: {self.password}, \nактивность: {self.active}\n')

user_1 = User()
user_1.print_info()

user_2 = User()
user_2.name = "Nimda"
user_2.print_info()