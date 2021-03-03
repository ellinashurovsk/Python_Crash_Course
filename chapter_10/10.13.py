import json


def get_stored_username():
    """
    Получает хранимое имя пользователя, если оно существует.
    """
    filename = "username.json"
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    Запрашивает новое имя пользователя.
    """
    filename = "username.json"
    username = input("Enter your name:")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """
    Приветствует пользователя по имени.
    """
    username = get_stored_username()
    if username:
        print(f"Are you {username}? Enter yes/no.")
        answer = input()
        if answer == "yes" or answer == "Yes":
            print(f"Welcome back {username}.")
        else:
            get_new_username()
            print(
                f"We will remember you when you  {get_stored_username().title()}")
    else:
        username = get_new_username()
        print(f"We will remember you when you come back {username}")


greet_user()
