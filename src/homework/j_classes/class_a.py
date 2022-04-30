# HW 9
import random

class Die:

    def roll(self):
        __roll_value = random.randint(1,6)
        return __roll_value

    def get_roll_value(self):
        return self.roll()

    def __str__(self):
        return str("The rolled value is {0}".format(self.get_roll_value()))