import json

filename = 'favorite_number.json'
input_name = input('Please enter your favorite number! ')

with open(filename, 'w') as file_obj:
    json.dump(input_name, file_obj)
