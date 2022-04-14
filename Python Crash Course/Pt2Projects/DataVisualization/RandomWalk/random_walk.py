# A random walk are random points which we will plot, like plotting a confused ant's walk
# Random walks model many real world things in nature, like pollen floating over water
from random import choice


# Now we will make a randomwalk() class to make random decisions
class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=50000):    # Set number of points we will create to 5000
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0] # Make a list to hold x and y values, starting at (0, 0)
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points: # Loop continues until number of steps is completed
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])   # Choose between moving left or right
            x_distance = choice([0, 1, 2, 3, 4])    # Choose how far we will go in that direction
            x_step = x_direction * x_distance   # Determine length of step by multiplying direction and distance
                                                # If -1 then the distance will move left
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0: # Tell loop to ignore moves that go no where
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step  # To get the value of the next step we add the value in list by new value
            y = self.y_values[-1] + y_step

            self.x_values.append(x)     # Append the new value to the list
            self.y_values.append(y)

