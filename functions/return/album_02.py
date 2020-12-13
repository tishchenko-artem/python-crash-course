def make_album(singer:str, album_name:str, quantity_tracks=''):
    '''Функция принимает на вход две строки,
    добавляет эти две строки в виде значений в словарь и возвращает этот словарь.'''
    album = {'author': singer.title(), 'album': album_name.title()}
    if quantity_tracks:
        album['tracks'] = quantity_tracks
    return album

while True:
    print('Please enter name of singer, name of your favorite album and number of tracks in this album')
    print('Enter "q" if you want to finish')
    print()
    s_name = input('Singer: ')
    if s_name == 'q':
        break
    a_name = input('Album: ')
    if a_name == 'q':
        break
    t_quantity = input('Number of tracks: ')
    if t_quantity == 'q':
        break
    print()

    new_album = make_album(s_name, a_name, t_quantity)
    print(new_album)
    print()

