# Json files are very dense and written for machines, but there are great modules for viewign them
# This data has locations and sizes of earthquaes, which will use pyplot to put them on a map
# Right now we will load the data and load good info to another file, which we will then read
import json

from plotly.graph_objs import Scattergeo, Layout    # IMport scattergeo type chart and layout class
from plotly import offline  # IMport offline module to render map

# Explore the structure of data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:   # Load data from file
    all_eq_data = json.load(f)  # Store entire set of data in all_eq_data
'''
readable_file = 'data/generated_data/readable_eq_data.json' # Create a new file to write same data in readable format
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) # json.dump() takes JSON data object and writes data to that file
                                        # Indent-4 argument tells dump() to use indentation to match data structure
'''
# When you look at the data in the file there is a "metadata" section which shows information on the date
# The information is when file was created, where data is online, readable title, and how many earthquakes occured
# geoJSON file has structure which is helpful for location based data
# Info is stored in a list associated with key 'features'
# This structure has data stored in dictionaries, like when data for a spacific earthquake is stored in one dictionary
# The key 'properties' contains info on each earthquake, like magnitude, which is tied to keyword 'mag'
# geoJASON follows the (longitude, latitude) location formatting

all_eq_dicts = all_eq_data['features']  # This code is small but it can efficiently find all earthquakes from 6000 lines
# print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []   # Empty list to store magnitudes
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Each Earthquake magnitude is stored in 'properties' section under 'mag'
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']  # Store title data from dictionary to a variable
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)   # Append the descriptive texts to list hover_texts
# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

# Map the earthquakes
data = [{   # Define list and create scattergeo object inside this list
    'type': 'scattergeo',    # Scattergeo type chart overlays scatterplot of geo data with lat and long points
    'lon': lons,
    'lat': lats,
    'text': hover_texts,    # Include key 'text' to display text when we hover over it
                            # Plotly uses this value assigned to it to come up with a label to put on any data point
    'marker': {  # Use key 'marker' to specify how big each marker on a map should be
        'size': [5*mag for mag in mags], # Use list comprehension to make an appropriate marker size for magnitude
        'color': mags,  # Color tells plotly what values it should use to determine where a marker is on the colorscale
        'colorscale': 'Viridis',    # Use the viridis colorscale to give values their color (blue to yellow)
        'reversescale': True,   # Set True so yellow is used for low eartquakes and blue is used for powerful ones
        'colorbar': {'title': "Magnitude"}, # Allows control a colorscale on side of the map to show color severity
    },
}]
# All changes to appearance are in the marker dictionary
# There are many key value pairs which can be used in this module for customization of graphs

# You could use another format if you don't include the marker feature
# data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title='Global Earthquakes')  # Give chart a title

fig = {'data': data, 'layout': my_layout}   # Create dictionary which contains data and the layout
offline.plot(fig, filename='global_earthquakes.html')   # pass fig to the plot() function with a filename for output
