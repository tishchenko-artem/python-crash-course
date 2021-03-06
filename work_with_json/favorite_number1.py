import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        name = json.load(file_object)
        print('Я знаю ваше любимое число! Это ' + name)
except FileNotFoundError:
    input_name = input('Please enter your favorite number! ')
    with open(filename, 'w') as file_obj:
        json.dump(input_name, file_obj)




