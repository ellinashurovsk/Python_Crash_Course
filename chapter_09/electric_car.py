from car import Car


class Battery():
    def __init__(self, battery_size=75):
        """ Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """ Выводит информацию о мощности аккумулятора."""
        print(f"This car has {self.battery_size}-kWH battery.")

    def get_range(self):
        """ Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        else:
            print(f"The battery size is {self.battery_size}.")


class ElectricCar(Car):
    """  Представляет аспект машины, специфические для электромобилей."""

    def __init__(self, manufacturer, model, year):
        """ Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(manufacturer, model,
                         year)  # функция super() - специальная функция, которая позволяет вызвать метод родительского класса
        self.battery = Battery()

    def fill_gas_tank(self):
        """ An electric car doesn't need a gas tank."""
        print("This car doesn't have  a gas tank!")


my_tesla_car = ElectricCar("tesla", "model s", "2019")
print(my_tesla_car.get_descriptive_name())
my_tesla_car.battery.describe_battery()
my_tesla_car.battery.get_range()
my_tesla_car.battery.upgrade_battery()
my_tesla_car.battery.get_range()
