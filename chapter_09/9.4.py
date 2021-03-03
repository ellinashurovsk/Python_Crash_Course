class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
        print()

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, incrementor_of_the_number):
        self.number_served += incrementor_of_the_number


restaurant = Restaurant('Mir pizzi', 'Italian')
print(restaurant.number_served)
restaurant.set_number_served(500)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.number_served)
