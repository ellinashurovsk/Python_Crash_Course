class Car():
    """A simple attempt to represent a car."""

    # определяется метод __init__(), с параметрами self, manufacturer, model, year.
    def __init__(self, manufacturer, model, year):
        # Метод __init__() получает эти параметры и сохраняет их в атрибутах, которые будут связаны с экземплярами, созданными на основе класса.
        """Initialize the discription attributes of the car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        # создание нового атрибута и присваивание ему исходного значения 0
        self.odometr_reading = 23

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name

    def update_odometr(self, mileage):
        """ Устанавливает заданное значение на одометре."""
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometr!")

    def read_odometr(self):
        """Выводит пробег машины в милях"""
        print(f"This car has {self.odometr_reading} miles on it.")

    def increment_odometr(self, miles):
        """ Увеличивает показания одометра с заданым приращением."""
        if miles >= 0:
            self.odometr_reading += miles
        else:
            print("You can't roll back an odometr!")

    def fill_gas_tank(self):
        """ Напоминание о заправке бака."""
        print("Please fill in a gas tank!")


# my_new_car = Car("Audi", "A4", "2010")
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometr(23500)
# my_new_car.read_odometr()
# my_new_car.increment_odometr(100)
# my_new_car.read_odometr()
