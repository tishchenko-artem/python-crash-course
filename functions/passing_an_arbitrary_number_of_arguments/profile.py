def my_profile(first_name, last_name, *other_info):
    '''Функция принимает два обязательных аргумента и произвольное количество остальных аргумнтов.'''
    print('\n' + first_name + ' ' + last_name + ':')
    for value in other_info:
        print(value)


user_profile = my_profile('Artem', 'Tishchenko', 'Ukraine', 'Computer Science', 'M')
print(user_profile)
