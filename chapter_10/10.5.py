while True:
    the_reason = input("Why do you like programming? (Enter \"q\" to quit) ")
    if the_reason == "q":
        break
    with open("10\\reasons.txt", 'a') as file_object:
        file_object.write(f"{the_reason} \n")
