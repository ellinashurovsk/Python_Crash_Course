class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name}')
        print(f'{self.last_name}')
        print(f'{self.age}')
        print(f'{self.location}')
        print()

    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


billi_user = User("Billi", "Smith", "20", "California")
billi_user.increment_login_attempts()
billi_user.increment_login_attempts()
billi_user.increment_login_attempts()
print(billi_user.login_attempts)
billi_user.reset_login_attempts()
print(billi_user.login_attempts)
