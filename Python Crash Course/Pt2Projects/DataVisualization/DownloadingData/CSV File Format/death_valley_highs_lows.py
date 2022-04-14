import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:   # Open file and assign result to f
    reader = csv.reader(f)  # call csv.reader() and pass file object as argument to create a reader object of that file
    header_row = next(reader)   # Call next to read the first line, and assign that line to header_row

    # Get dates and highs and lows from this file
    dates, highs, lows = [], [], []  # Create empty lists
    for row in reader:  # Loop through remaining rows in file
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:    # If any data is missing python will raise a valuerror and skip over the missing data point
            high = int(row[4])  # On each line pull data from index 5, which is the TMAX
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}. ")
        else:   # After an error, python will keep printing the other rows, and the regular program can run
            dates.append(current_date)
            highs.append(high)  # append this value to the highs list
            lows.append(low)

# Plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)   # Alpha value controls opacity, 0 is transparent and 1 is opaque
ax.plot(dates, lows, c='blue', alpha=0.5)   # Alpha 0.5 makes plot lines appear lighter
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # fill_between fills space between plots with facecolor
                                            # Facecolor determines color, and alpha makes it non distracting
# Format plot
title = "Daily high and low temp - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)    # Set title, fontsize, and labels
ax.set_xlabel('', fontsize=16)  # We don't add dates yet, but set size to 16 so that default labels are easy to read
fig.autofmt_xdate() # This call draws date labels diagonally to prevent them from overlapping
ax.set_ylabel("Temperature (F) ", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()