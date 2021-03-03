from user import User


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
