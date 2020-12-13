def make_album(singer:str, album_name:str, quantity_tracks=''):
    '''Функция принимает на вход две строки,
    добавляет эти две строки в виде значений в словарь и возвращает этот словарь.'''
    album = {'author': singer.title(), 'album': album_name.title()}
    if quantity_tracks:
        album['tracks'] = quantity_tracks
    return album

music_album = make_album('alt j', 'an awesome wave')
music_album1 = make_album('elvis presley', 'blue moon')
music_album2 = make_album('pixies', 'surfer rosa')
music_album3 = make_album('pixies', 'surfer rosa', 7)

print(music_album)
print(music_album1)
print(music_album2)
print(music_album3)