from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        side = randint(1, self.sides)
        return side


die_10 = Die(10)
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print(die_10.roll_die())
print()

die_20 = Die(20)
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
print(die_20.roll_die())
