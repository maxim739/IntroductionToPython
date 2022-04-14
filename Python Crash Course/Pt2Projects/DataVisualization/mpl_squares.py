import matplotlib.pyplot as plt  # Import pyplot module with plt alias so we don't have to rewrite it a lot

# Here we will give matplotlib lib a set of numbers and it will square them and make a graph
input_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]  # Create a list of numbers

plt.style.use('seaborn')    # There are many styles that come with matplotlib, check them using plt.style.avaliable
fig, ax = plt.subplots()  # Call subplots() function, which generates one or more plots on the same figure
# The variable fig represents the entire figure or collection of points generated
# The variable ax is a variable representing a single plot on the figure
ax.plot(input_values, squares, linewidth=3)  # Use plot() to plot the data it is given in a meaningful way
# Linewidth controls how thick the line is that plot() generates

# Set chart title and label axis.
ax.set_title("Square numbers", fontsize=24) # Sets title for graph, and font determines title size
ax.set_xlabel("Value", fontsize=14) # Both set a title for each axis and fontsize determines how big they are
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)   # Method tick_params() style the tick marks

plt.show()  # Opens matplotlib lib's viewer and displays the plot

# When you give plot() a series of numbers it assumes the first data point correlates to an x coordinate value of 0
# This is overridden when you give plot() the input and output values used to calculate the squares
