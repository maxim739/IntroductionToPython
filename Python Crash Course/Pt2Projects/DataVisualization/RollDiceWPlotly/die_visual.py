from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store the results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze results
frequencies = []    # Create an empty list to store the number of times each value is rolled
for value in range(1, die.num_sides+1): # Loop through possible values
    frequency = results.count(value)    # Count how many times each number appears in results list
    frequencies.append(frequency)   # Append value of times to frequencies list

# Visualize the results
x_values = list(range(1, die.num_sides+1))   # Make bar for each possible result and store them in x_values
                                            # Plotly dosen't accept range() functions so its converted into a list
data = [Bar(x=x_values, y=frequencies)]  # Class Bar() represents a data set that will be formatted as a bar chart
                                        # Class needs list of x values and y values
                                        # Wrapped in square brackets bc data set can have multiple elements
x_axis_config = {'title': 'Result'} # Set title of each axis
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',# Layout class returns an object specifies configuration
                   xaxis=x_axis_config, yaxis=y_axis_config)    # Set title of graph and x/y config dictionaries
offline.plot({'data': data, 'layout':my_layout}, filename='d6.html')    # Call offline.plot() to generate plot
# This function needs a dictionary containing data and layout objects, and also accepts a name for where file is saved
# This file will open up in a browser

print(frequencies)