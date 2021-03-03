import json

filename = "favorite_number111.json"

try:
    with open(filename, 'r') as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    with open(filename, 'w') as file_object:
        favorite_number = input("Enter your favorite number:")
        json.dump(favorite_number, file_object)
        print(f"I will remember your favorite number {favorite_number}.")
else:
    print(f"Your favorite file name is {favorite_number}.")
