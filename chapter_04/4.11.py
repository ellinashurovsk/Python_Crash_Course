pizzas = ["pepperoni", "4 chese", "margarita", "royal", "vegeterian"]
friend_pizzas = pizzas[:]


pizzas.append("falafel")
print("\n\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

friend_pizzas.append("meat pizza")

print("\n\nMy friend favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
