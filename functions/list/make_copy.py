favorite_magicians = ['Artem', 'Viktor', 'Anatoliy', 'Nikita']
new_list = []

def make_great(mag:list):
    '''Функція приймає копію списку  та повертає новий список new_list с приставкою "Great".'''
    for magician in mag:
        new_list.append("Great " + magician + " !")
    return new_list

def show_magicians(old_list, new_list):
    '''Функція виводить на екран два списки.'''
    for magician in old_list:
        print(magician)
    for great_magician in new_list:
        print(great_magician)


great_show = make_great(favorite_magicians[:])
print_magicians = show_magicians(favorite_magicians, new_list)
