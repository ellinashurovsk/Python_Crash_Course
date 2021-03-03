dct = {}

while True:
    message1 = "What is your name? "
    message2 = "What country would you like to visit? "
    name = input(message1)
    if name == 'quit':
        break
    country = input(message2)
    dct[name] = country
print()

for key, value in dct.items():
    print("Name: "+f"{key}"+"\nCountry: "+f"{value}")
