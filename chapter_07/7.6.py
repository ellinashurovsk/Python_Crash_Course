message = "\nPlease enter the topping: "
topping = ""
active = True

while active:
    topping = input(message)
    if topping == 'quit':
        active = False
        break
    if topping != 'quit':
        print(f"You have added the {topping} topping.")
