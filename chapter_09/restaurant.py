# 9.1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}")
        print(f"{self.cuisine_type}")
        print()

    def open_restaurant(self):
        print("The restaurant is open")


# my_restaurant = Restaurant('Mir pizzi', 'Italian')
# print(f"{my_restaurant.restaurant_name}")
# print(f"{my_restaurant.cuisine_type}")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
