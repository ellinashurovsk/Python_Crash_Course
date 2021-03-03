from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanila"]

    def show_flavors(self):
        print("\nThe flavors are: ")
        for i in self.flavors:
            print(i)


my_ice_restaurant = IceCreamStand("Ice-Ice", "Ice-Cream restaurant")
my_ice_restaurant.show_flavors()
