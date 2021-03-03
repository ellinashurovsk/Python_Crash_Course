class Employee():
    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, increase=5000):
        increased_salary = self.salary + increase
        return increased_salary
