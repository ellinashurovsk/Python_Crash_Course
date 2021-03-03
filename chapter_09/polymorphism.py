class Sum():
    """ Подкрепляет идеи полиморфизма."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_a_b(self):
        """ Суммирует два числа: a, b."""
        return self.a+self.b


my_class = Sum("10", "10")
print(my_class.sum_a_b())

my_class = Sum(10, 10)
print(my_class.sum_a_b())
