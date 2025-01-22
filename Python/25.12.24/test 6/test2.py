from test1 import User


user_1 = User("Admin", "qwerty", True)
user_2 = User("Nimda", "qwerty", True)


user_1.add_friends("Tom")
user_1.add_friends("Jerry")
user_1.add_friends(user_2)

user_1.print_info()