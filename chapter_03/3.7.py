names = ["Masha", "Charlotte", "Harper"]

names.insert(0, "Tanya")
names.insert(2, "Katya")
names.append("Nick")

print(f"An invitation for you, {names[0]}.")
print(f"An invitation for you, {names[1]}.")
print(f"An invitation for you, {names[2]}.")
print(f"An invitation for you, {names[3]}.")
print(f"An invitation for you, {names[4]}.")
print(f"An invitation for you, {names[5]}. \n")


print("Very sorry but there are only 2 places")

popped_person = names.pop()
print(f"Very sorry, but you are not invited {popped_person}.")
popped_person = names.pop()
print(f"Very sorry, but you are not invited {popped_person}.")
popped_person = names.pop()
print(f"Very sorry, but you are not invited {popped_person}.")
popped_person = names.pop()
print(f"Very sorry, but you are not invited {popped_person}.\n")

print(f"An invitation for you, {names[0]}.")
print(f"An invitation for you, {names[1]}. \n")

del names[1]
del names[0]

print(names)
