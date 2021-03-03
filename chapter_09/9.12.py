from user import User
from privileges import Privileges
from admin import Admin


admin_Sam = Admin("Sam", "Smith", 50, "NY")
admin_Sam.privileges.show_privileges()
