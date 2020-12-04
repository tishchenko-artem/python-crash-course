def make_shirt(size='L', text='I love Python'):
    """Функция выводит размер футболки и текст, который должен быть на ней напечатан."""
    return 'Размер вашей футболки: {}. Текст, который на ней будет напечатан: "{}".'.format(size, text)


print(make_shirt())
print(make_shirt('M', 'Hello'))
