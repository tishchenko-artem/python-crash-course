class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant ' + '"' + self.restaurant_name.title() + '"' + ' ' + self.cuisine_type.lower() + ' cuisine'
              + ', ' + str(self.number_served) + ' visitors were served')

    def open_restaurant(self):
        print("Restaurant is open now")

    def set_number_served(self, served_customers):
        self.number_served = served_customers

    def increment_number_served(self, customers):
        if customers >= 0:
            self.number_served += customers
        else:
            print('You cannot serve a negative number of customers')


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def print_flavours(self):
        print('Ice cream flavors are currently available:')
        for el in self.flavours:
            print(el)

IceCream = IceCreamStand('Velour', 'ukrainian', ['chocolate', 'milk', 'strawberry'])
IceCream.print_flavours()

# restaurant1 = Restaurant('velour', 'ukrainian')
# restaurant1.set_number_served(0)
# restaurant1.increment_number_served(-3)
# restaurant1.describe_restaurant()

# restaurant2 = Restaurant('Eleven Madison Park', 'american')
# restaurant3 = Restaurant('Mirazur', 'French')

# print(restaurant1.describe_restaurant())
# print(restaurant2.describe_restaurant())
# print(restaurant3.describe_restaurant())

# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# print(restaurant.describe_restaurant())
# print(restaurant.open_restaurant())
