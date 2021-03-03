countries = ["France", "Germany", "Finland", "Estonia", "Egypt"]

print(countries)

""" Функция sorted() сохраняет исходный порядок элементов 
списка, но временно представляет их в отсортированном порядке"""
print(sorted(countries))

print(countries)

# Аргумент reverse=True - список представлен в обратном порядке.
print(sorted(countries, reverse=True))

print(countries)
print()

countries.reverse()
print(countries)

countries.reverse()
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)
