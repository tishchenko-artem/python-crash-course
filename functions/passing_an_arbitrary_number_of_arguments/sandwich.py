def sandwiches(*toppings):
    '''Функция принимает произвольное количество значений и возвращает описания сэндвичей.'''
    print('\nYour sandwich is ready:')
    for topping in toppings:
        print('- ' + topping.lower() + ';')


first_sandwich = sandwiches('cheese')
second_sandwich = sandwiches('becon', 'tomato')
third_sandwich = sandwiches('cheese', 'becon', 'tomato')
