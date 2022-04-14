import re  # Import regular expressions module

message = ('Call me at 802-324-0612 or 802-802-8022')  # Make a message

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #  re.compile function
# Use raw strings in re.compile(), which are strings but with the lowercase r at the front
# The backslash is used to signify characters, and raw strings use them a lot
# d stands for digit
# Pass the re.compile function where we pass our string through
# Make the pattern we are looking for
# d stands for a digit seperated with backslashges
# We look for this pattern and store it as an object
mo = phoneNumRegex.search(message)  # Now we will search the string for that pattern, returned as a matched object
# This is a search method in re which will find the pattern in a string. It will look for that pattern in the string
# We also stored the value as a matched object
print(mo.group())  # Now group() will tell us the text that is in the matched object

# This only returns the first instance of this pattern, if we want to find all we will use finall()
mo2 = phoneNumRegex.findall(message)
print(mo2)
# This will print out a list of string values
# It will find every occurence of this patter