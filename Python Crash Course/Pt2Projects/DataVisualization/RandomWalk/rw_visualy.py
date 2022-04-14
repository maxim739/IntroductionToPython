import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making walks as long as program is active
while True:
    # Make a random walk
    rw = RandomWalk(50_000)   # Create a randomwalk and store it in rw
    rw.fill_walk()  # Call fillwalk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()    # Add plt.subplots(figsize=(15, 9)) to set size of graph
                                # This is based on a resolution of 100 pixels per inch
                                # Use plt.subplots(figsize=(10, 6), dpi=128) using dpi paramater to be more effective
    point_numbers = range(rw.num_points)    # Create list of numbers equal to number of points on walk
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)  # Feed x and y
    # Also disable borders around points and add colormap
    # Emphasize first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)   # Plot point (0, 0)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=1) # Plot last point in the lists

    # Remove the axis
    ax.get_xaxis().set_visible(False)   # This method sets the visibility of each axis to False
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n' or keep_running == 'q':
        break