from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two dice
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store the results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()    # Calculate sum of two dice for each roll
    results.append(result)

# Analyze results
frequencies = []    # Create an empty list to store the number of times each value is rolled
max_result = die_1.num_sides + die_2.num_sides  # The largest possible result is sum of both largest number on dice
for value in range(2, max_result+1): # Count number of results between two and max_result
    frequency = results.count(value)    # Count how many times each number appears in results list
    frequencies.append(frequency)   # Append value of times to frequencies list

# Visualize the results
x_values = list(range(2, max_result+1))   # Make bar for each possible result and store them in x_values
                                            # Plotly dosen't accept range() functions so its converted into a list
data = [Bar(x=x_values, y=frequencies)]  # Class Bar() represents a data set that will be formatted as a bar chart
                                        # Class needs list of x values and y values
                                        # Wrapped in square brackets bc data set can have multiple elements
x_axis_config = {'title': 'Result', 'dtick': 1}     # Include dtick in x_axis_config dictionary controls tick marks
                # 'dtick': 1 setting tells plotly to label every tick mark
y_axis_config = {'title': 'Frequency of result'}    # Set title of each axis
my_layout = Layout(title='Results of rolling a D6 and D10 50,000 times',# Layout class returns object specifies configuration
                   xaxis=x_axis_config, yaxis=y_axis_config)    # Set title of graph and x/y config dictionaries
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')    # Call offline.plot() to generate plot
# This function needs a dictionary containing data and layout objects, and also accepts a name for where file is saved
# This file will open up in a browser

print(frequencies)