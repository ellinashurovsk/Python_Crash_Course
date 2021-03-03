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


class Privileges():
    def __init__(self, admin_privileges=["разрешено добавлять сообщения",
                                         "разрешено удалять пользователей",  "разрешено банить пользователей"]):
        self.admin_privileges = admin_privileges

    def show_privileges(self):
        print("\nThe privileges for the admin are:")
        for i in self.admin_privileges:
            print(i)


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
