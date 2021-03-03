sandwich_orders = ["Beef Sandwich.",
                   "Cheese Sandwich.",
                   "Pastrami Sandwich",
                   "Chicken Sandwich.",
                   "Ham Sandwich.",
                   "Pastrami Sandwich",
                   "Pork Sandwich.",
                   "Tuna Sandwich.",
                   "Pastrami Sandwich",
                   "Turkey Sandwich."]
finished_sandwiches = []
print("There is no more Pastrami Sandwich!\n ")

while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a "+f'{sandwich}')
    finished_sandwiches.append(sandwich)
print()
for sandwichh in finished_sandwiches:
    print(sandwichh)
