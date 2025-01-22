class User:
    def __init__(self, name, password, active):
        self.name = name
        self.password = password
        self.active = active
        self.friends = []


    def print_info(self):
        print(f'Имя: {self.name}, \nпароль: {self.password}, \nактивность: {self.active}, \nдрузья: {self.friends}\n')

    def add_friends(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.name)
        else:
            self.friends.append(friend)