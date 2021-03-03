favorite_numbers = {
    'James': {'1': '5', '2': '9', },
    'Ava': {'1': '6', '2': '18', },
    'Harper': {'1': '8', '2': '3', },
    'Alisa': {'1': '100', '2': '40', },
    'Lucas': {'1': '600', '2': '50', },
}

for name, value in favorite_numbers.items():
    print(name)
    frst = value['1']
    second = value['2']
    print('Favorite numbers: '+frst+','+second)
    print('\n')
