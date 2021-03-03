def make_album(musician, album_title):
    album = {'musician': musician, 'title': album_title}
    return(album)


while True:
    print("Enter the musician.")
    print("(Enter\"q\" to quit)")
    musician_while = input()
    if musician_while == "q":
        break
    print("Enter album title.")
    print("(Enter \"q\" to quit)")
    album_title = input()
    if album_title == "q":
        break
    album_while = make_album(musician_while, album_title)
    print(album_while)
