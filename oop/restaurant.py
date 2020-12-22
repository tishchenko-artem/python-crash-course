class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant ' + '"' + self.restaurant_name.title() + '"' + ' ' + self.cuisine_type.lower() + ' cuisine')

    def open_restaurant(self):
        print("Restaurant is open now")


restaurant1 = Restaurant('velour', 'ukrainian')
restaurant2 = Restaurant('Eleven Madison Park', 'american')
restaurant3 = Restaurant('Mirazur', 'French')

print(restaurant1.describe_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# print(restaurant.describe_restaurant())
# print(restaurant.open_restaurant())
