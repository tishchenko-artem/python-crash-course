from magicians import favorite_magicians


def make_great(mag:list):
    '''Функція приймає список фокусників з файлу magicians.py та повертає відрадактовані вітання.'''
    for magician in favorite_magicians:
        print("Great " + magician + ' !')


great_show = make_great(favorite_magicians)

print(great_show)
