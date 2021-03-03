sandwich_orders = ["Beef Sandwich.",
                   "Cheese Sandwich.",
                   "Chicken Sandwich.",
                   "Ham Sandwich.",
                   "Pork Sandwich.",
                   "Tuna Sandwich.",
                   "Turkey Sandwich."]
finished_sandwiches = []


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a "+f'{sandwich}'+"\n")
    finished_sandwiches.append(sandwich)

for sandwichh in finished_sandwiches:
    print(sandwichh)
