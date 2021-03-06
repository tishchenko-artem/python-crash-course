import json

with open('favorite_number.json') as file_object:
    name = json.load(file_object)

print('Я знаю ваше любимое число! Это ' + name)