rivers = {"nile": "egypt", "Volga": "Russia", "Seina": "France"}

for key, value in rivers.items():
    print(f"{key.title()} is the river that runs through {value.title()}.")
print("\n")
for i in rivers:
    print(i.title())

for keys in rivers.keys():
    print(keys.title())
print("\n")
for i in rivers:
    print(rivers[i].title())
for value in rivers.values():
    print(value.title())
