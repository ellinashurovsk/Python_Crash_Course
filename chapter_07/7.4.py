message = "\nPlease enter the topping: "
topping = ""

while topping != "quit":
    topping = input(message)
    if topping != 'quit':
        print(f"You have added the {topping} topping.")
