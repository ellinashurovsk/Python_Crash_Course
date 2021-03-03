import json

filename = "file_with_number.json"
with open(filename, 'w') as file_object:
    number = input("Enter your favorite number: ")
    json.dump(number, file_object)


with open(filename, 'r') as f:
    fav_number = json.load(f)
    print(f"I know your favorite number. It is {fav_number}")
