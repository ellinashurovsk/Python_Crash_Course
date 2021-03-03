# #ЧТЕНИЕ ИЗ ФАЙЛА
# with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())  # удаление лишней пустой строк


# # ЧТЕНИЕ ПО СТОРОКАМ
# with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())


# # СОЗДАНИЕ СПИСКА СТРОК ПО СОДЕРЖИМОМУ ФАЙЛА
# with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())


# РАБОТА С СОДЕРЖИМЫМ ФАЙЛА
# with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
#     lines = file_object.readlines()

# final_line = ''
# for line in lines:
#     final_line += line.strip()

# print(final_line)


# МИЛЛИОН цифр
# with open('10\\pi_digits_million.txt') as file_object:
#     lines = file_object.readlines()

# final_line = ''
# for line in lines:
#     final_line += line.strip()

# bithday = input("Enter your bithday in the form of ddmmyy: ")
# if bithday in final_line:
#     print("Your bithday is in pi number!")
# else:
#     print("Your bithday is not in pi number:(")


# ЗАПИСЬ В ФАЙЛ
# filename = '10\\programming.txt'
# with open(filename, 'w') as file_object:  # РЕЖИМ ЗАПИСИ
#     file_object.write("I love programming.\n")

# with open(filename, 'a') as file_object:  # РЕЖИМ ПРИСОЕДИНЕНИЯ
#     file_object.write("I also like finding meaning in large datasets.\n")
#     file_object.write("I also like electrical engineering.\n")
#     file_object.write("I also like my cat <3\n")


# ИСКЛЮЧЕНИЯ

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You can\'t divide by zero!'
#     )

# try:
#     with open("10\\lear ning_python.txt") as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     print("Sorry, the file is not found!")
# else:
#     lst = []
#     lst = contents.split()
#     print(len(lst))


# СОХРАНЕНИЕ ДАННЫХ

# import json

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# # filename = 'numbers.json'
# # with open(filename, 'w') as f:
# #     json.dump(numbers, f)

# filename = 'numbers.json'
# with open(filename, 'r') as f:
#     numbers = json.load(f)

# print(numbers)


import json


def greet_user():
    """User greetings
    """
    try:
        with open("user.json", 'r') as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("Please enter your name: ")
        with open("user.json", 'w') as file_object:
            json.dump(username, file_object)
            print(
                f"We will remember you when you come back {username.title()}")
    else:
        print(f'Welcome back {username}')


greet_user()
