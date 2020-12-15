favorite_magicians = ['Artem', 'Viktor', 'Anatoliy', 'Nikita']


def show_magicians(mag: list):
    '''Проста функція, яка виводить на екран імена фокусників.'''
    for name in mag:
        print(name)

show = show_magicians(favorite_magicians)
print(show)