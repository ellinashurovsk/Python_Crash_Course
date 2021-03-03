def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    person = (f"{first_name.title()}"+f" {last_name.title()}")
    return(person)


# This is an infinite loop!
while True:
    print("\nPlease tell me your first name.")
    print("(enter \"q\" to quit)")

    f_name = input()
    if f_name == "q":
        break

    print("\nPlease tell me your last name.")
    print("(enter \"q\" to quit)")

    l_name = input()
    if l_name == "q":
        break

    person1 = get_formatted_name(f_name, l_name)
    print(f"\nHello, {person1}")

formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
