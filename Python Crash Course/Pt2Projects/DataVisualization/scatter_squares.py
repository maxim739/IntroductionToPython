import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)  # Call scatter and use the s= argument to set the size of the dots

# Set chart title and label axis
ax.set_title("Square numbers", fontsize=24)  # Sets title for graph, and font determines title size
ax.set_xlabel("Value", fontsize=14)  # Both set a title for each axis and fontsize determines how big they are
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)  # Method tick_params() style the tick marks

plt.show()
