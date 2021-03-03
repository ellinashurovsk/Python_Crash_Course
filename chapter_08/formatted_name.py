def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        person = (
            f"{first_name.title()} {middle_name.title()} {last_name.title()}")
    else:
        person = (f"{first_name.title()} {last_name.title()}")
    return person


print(get_formatted_name("Adam", "Smith", "Erich"))
