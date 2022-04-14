from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)

# IF you print this dictionary you can see how colorscales are defined. Every colorscale has a beginning and end
# color With some having intermediate colors, but plotly interprets the shades between these two colors and assigns
# them to values
