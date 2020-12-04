def describe_city(city, country='Ukraine'):
    '''Функция возвращает простое сообщение, которое сообщает
     в какой стране находится определенный город.'''
    return '{} is in {}'.format(city, country)

print(describe_city(city='Kyiv'))
print(describe_city(city='Odessa'))
print(describe_city(city='Berlin', country='Germany'))