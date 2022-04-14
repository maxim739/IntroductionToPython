import matplotlib.pyplot as plt

x_values = range(1, 1001)  # X values are a range from 1 to 1000
y_values = [x ** 2 for x in x_values]
# List comprehension generates y values by squaring every number in the x_values list

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# You can use built in colormaps to give higher y values a different color for e.g
# Specify how pyplot assigns colors with the c=y_values
# Pass list of y-values to c, and tell pyplot which colormap to use in the cmap argument
# This will give higher y values a dark blue
# Check colormaps avaliable at https://matplotlib.org/, then go to Examples, then Colormap refrence

# Pass inputs and outputs through scatter()
# Define custom colors with ax.scatter(x_values, y_values, c='red', s=10
# Or you can do it with ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10) and use the RGB decimals between 0 and 1

# Set chart title and label axis
ax.set_title("Square numbers", fontsize=24)  # Sets title for graph, and font determines title size
ax.set_xlabel("Value", fontsize=14)  # Both set a title for each axis and fontsize determines how big they are
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)  # Method tick_params() style the tick marks

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])
# axis() requires four values. Minimum and maximum for x and y axis.
# Order x axis from 0 to 1100, and y axis from 0 to 1,100,000

plt.show()
# If you want your graph to automatically save to your computer use
# plt.savefig('squares_plot.png', bbox_inches='tight')
# The first argument is the name of the file, and the second trims extra whitespace from the plot
# If you want to save the whitespace just omit the second argument

# Python can plot 1000 points as easily as 5 points
