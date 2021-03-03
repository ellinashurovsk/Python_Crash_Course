# 9.3
class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f'{self.first_name}')
        print(f'{self.last_name}')
        print(f'{self.age}')
        print(f'{self.location}')
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        print()
