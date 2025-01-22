class User:
    name = "Admin"
    password = "qwerty"
    active = True
    friends = []

    def print_info(self):
        print(f'Имя: {self.name}, \nпароль: {self.password}, \nактивность: {self.active}, \nдрузья: {self.friends}\n')

    def add_friends(self, friend):
        self.friends.append(friend)

user_1 = User()
user_1.print_info()

user_2 = User()
user_2.name = "Nimda"
user_2.add_friends("Tom")
user_2.print_info()