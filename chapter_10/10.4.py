while True:
    name = input("Enter your name. (Enter \"q\" to quit.)")
    if name == "q":
        break
    print(f"Hello, {name}")
    with open("10\\guest.txt", 'a') as file_object:
        file_object.write(f"{name.title()} \n")
