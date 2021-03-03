name = input()

with open("10\\guest.txt", 'w') as file_object:
    file_object.write(name.title())
