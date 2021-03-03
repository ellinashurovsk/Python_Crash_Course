def formatted_city_country(city, country, population=0):
    if population != 0:
        formatted_city_country = f"{city}, {country} - population {population}"
    else:
        formatted_city_country = f"{city}, {country}"
    return formatted_city_country
