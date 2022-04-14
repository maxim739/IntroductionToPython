from random import randint

class Die:
    """A class representing a single die"""
    def __init__(self, num_sides=6):    # Takes number of sides, otherwise default is 6
        """Assume single sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)   # Uses randint to find an int between num_sides and 1