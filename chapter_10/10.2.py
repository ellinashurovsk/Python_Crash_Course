with open("10\\learning_python.txt") as messages:
    for message in messages:
        print(message.replace('Python', 'C').rstrip())
