# def get_formatted_name(first, last):
#     """
#     Выдает полное имя. В качестве аргументов получает имя и фамилию.
#     """
#     full_name = f"{first.title()} {last.title()}"
#     return full_name


def get_formatted_name(first, last, middle=''):
    """
    Выдает полное имя. В качестве аргументов получает имя и фамилию.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name
