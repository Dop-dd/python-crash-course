class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")


    def open(self):
        print(f"The {self.restaurant_name} is open.")

chinese = Restaurant('Pekin', 'Noodles')
chinese.describe_restaurant()
chinese.open()
print('')

italian = Restaurant('Milan Tower', 'Pasta')
italian.describe_restaurant()
italian.open()
print('')

jamaican = Restaurant('Hot&Spicy', 'Jerk chicken')
jamaican.describe_restaurant()
jamaican.open()