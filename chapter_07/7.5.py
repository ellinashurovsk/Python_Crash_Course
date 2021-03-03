print("\nEnter your age: ", end='')
age = int(input())
price = 0

if age < 3:
    price = 0
elif age >= 3 and age < 12:
    price = 10
else:
    price = 15

print("The price is "+f"{price}"+"$.")
