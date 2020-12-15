def cars(manufacture, name, **other_info):
    '''Функция принимает два обязательные аргументы и произвольное количество именованных аргументов.'''
    car = {}
    car['manufacturer'] = manufacture
    car['model name'] = name
    for key, value in other_info.items():
        car[key] = value
    return car

model = cars('subaru', 'outback', color = 'blue', tow_package = True)
print(model)
