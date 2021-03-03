def city_country(city, country):
    text = f"{city.title()}, {country.title()}"
    return text


print()
text_ret = city_country("Santiago", "Chile")
print(text_ret)
text_ret = city_country("Moscow", "Russia")
print(text_ret)
text_ret = city_country("Helsinki", "Finland")
print(text_ret)
