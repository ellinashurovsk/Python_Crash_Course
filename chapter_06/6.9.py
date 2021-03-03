favorite_places = {
    'Elijah': {'first': 'Yellowstone National Park', 'second': 'Red Center', '3-rd': 'Bruges', },
    'Pekka': {'first': 'Lake Garda', 'second': 'Santorini', '3-rd': 'The Azores', },
    'Olivia': {'first': 'Tromso', 'second': 'Loire Valley', '3-rd': 'Venice', },
}

for name, value in favorite_places.items():
    print("\n Name: " + name)
    first = value['first']
    second = value['second']
    last = value['3-rd']

    print("\t First favorite place: " + first.title())
    print("\t 2-rd favorite place: " + second.upper())
    print("\t 3-rd favorite place: " + last.title())
