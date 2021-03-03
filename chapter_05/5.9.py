# names = ['Masha', 'Katya', 'Liza', 'Admin', 'Oleg']
names = []

if names:
    for name in names:
        if name == 'Admin':
            print('Hello, Admin, would you like to see a status report?')
        else:
            print(f'Hello, {name},thank you for logging in again!')

else:
    print('We need to find some users')
