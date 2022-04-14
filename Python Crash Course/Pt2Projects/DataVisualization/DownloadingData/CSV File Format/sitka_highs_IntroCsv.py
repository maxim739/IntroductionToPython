# CVS format stores data using commas , which can be very efficient
# The data we will use here is from Sitka alaska and death valley
# This data was downloaded from https://ncnd.noaa.gov/cdo-web/
# The CSV module lets us parse lines and make sense of how commas are seperating info
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:   # Open file and assign result to f
    reader = csv.reader(f)  # call csv.reader() and pass file object as argument to create a reader object of that file
    header_row = next(reader)   # Call next to read the first line, and assign that line to header_row
#    print(header_row)   # Open the header row to see headers for useful info

#    for index, column_header in enumerate(header_row):  # Enumerate() function returns index and value of items in list
#        print(index, column_header)
    # When we know how the data is stored we can start to extract it

    # Get dates and high temperatures from this file
    dates, highs = [], []  # Create empty lists
    for row in reader:  # Loop through remaining rows in file
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])  # On each line pull data from index 5, which is the TMAX
        dates.append(current_date)
        highs.append(high)  # append this value to the highs list
# print(dates, highs)

# Reader object continues from where it was in CSV file and returns each line following it's current position
# Because we have already used the header row, we will start on the second row where data begins



# Plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') # Use list of highs in plot() and set points to color red

# Format plot
ax.set_title("Daily high Temperatures - 2018 ", fontsize=24)    # Set title, fontsize, and labels
ax.set_xlabel('', fontsize=16)  # We don't add dates yet, but set size to 16 so that default labels are easy to read
fig.autofmt_xdate() # This call draws date labels diagonally to prevent them from overlapping
ax.set_ylabel("Temperature (F) ", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
