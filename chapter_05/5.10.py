current_users = ['Masha', 'Katya', 'Liza', 'Admin', 'Oleg']
new_users = ['Masha', 'KATYA', 'Olga', 'Ella', 'Konstantin']


for new_user in new_users:
    if new_user.title() in current_users:
        print('Please, choose a new user name.')
    else:
        print('The user name is chosen successfully.')
