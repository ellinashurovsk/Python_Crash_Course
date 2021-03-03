names = ["Oliver", "Charlotte", "Harper"]

print(f"An invitation for you, {names[0]}.")
print(f"An invitation for you, {names[1]}.")
print(f"An invitation for you, {names[2]}.\n")

print(f"{names[0].title()} can't be at the party.")

names[0] = "Masha"

print(f"An invitation for you, {names[0]}.")
print(f"An invitation for you, {names[1]}.")
print(f"An invitation for you, {names[2]}. \n")

print("Let's invite more people!\n")

names.insert(0, "Tanya")
names.insert(2, "Katya")
names.append("Nick")

print(f"An invitation for you, {names[0]}.")
print(f"An invitation for you, {names[1]}.")
print(f"An invitation for you, {names[2]}.")
print(f"An invitation for you, {names[3]}.")
print(f"An invitation for you, {names[4]}.")
print(f"An invitation for you, {names[5]}. \n")
