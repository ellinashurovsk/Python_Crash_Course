def print_file_contents(file_name):
    """
    Print the content of the function.
    file_name-str, the name of the file
    """
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("There is no file with such a name.")
    else:
        print(contents)


file_names = ["10\\cats.txt", "10\\dogs.txt"]
for file_name in file_names:
    print_file_contents(file_name)
