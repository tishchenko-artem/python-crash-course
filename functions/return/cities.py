def city_country(city, country):
    '''Функция принимает на вход две строки и возвращает отформатированную строку, состоящую из двух этих строк.'''
    message = city + ', ' + country
    return message.title()

city1 = city_country('santiago', 'Chile')
city2 = city_country('Kyiv', 'ukraine')
city3 = city_country('berlin', 'germany')

print(city1)
print(city2)
print(city3)