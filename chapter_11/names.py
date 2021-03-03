# программа импортирует функцию get_formatted_name из модуля name_function
from name_function import get_formatted_name

print("Enter \"q\" at any time to quit.")

while True:
    print("\nEnter your first name: ")
    first = input()
    if first == "q":
        break
    print("Enter your last name: ")
    last = input()
    if last == "q":
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
