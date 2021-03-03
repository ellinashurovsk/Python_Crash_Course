cities = {
    'Helsinki': {'Country': 'Finland', 'Population': '600 thousands', 'Fact': 'Suomenlinnya', },
    'Moscow': {'Country': 'Russia', 'Population': '20 million', 'Fact': 'Red Square', },
    'Paris': {'Country': 'France', 'Population': '2 million', 'Fact': 'Eiffel Tower', },
}

for city, value in cities.items():
    print(city)
    country = value['Country']
    population = value['Population']
    fact = value['Fact']
    print('Country: '+country.title())
    print('Population: '+population)
    print('Fact:'+fact+'\n')
