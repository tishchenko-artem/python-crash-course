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