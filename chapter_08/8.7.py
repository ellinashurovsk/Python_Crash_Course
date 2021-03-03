def make_album(musician, album_title, songs_amount=None):
    album = {'musician': musician, 'title': album_title}
    if songs_amount:
        album['songs_amount'] = songs_amount
    return album


album1 = make_album("Neighborhoods", "Blink-182")
album2 = make_album("The Score", "Atlas")
album3 = make_album("Britney", "Glory", 13)

print(album1)
print(album2)
print(album3)
