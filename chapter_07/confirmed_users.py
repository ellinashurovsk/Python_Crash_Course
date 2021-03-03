unconfirmed_users = ['Alice', 'Nick', 'Alex']
confirmed_users = []


while unconfirmed_users:  # пустые списки являются ложными
    # pop() удаляет последний элемент в списке и хранит его в памяти
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(confirmed_user)
