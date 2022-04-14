#Simple dictionary
alien0 = {'color': 'green', 'points': 5}
print(alien0['color'])
print(alien0['points'])
print("\n")

#A dictionary is made of key-value pairs
#You can provide a key, and it can give back a result or value

#Accessing Values in a Dictionary
alien = {'color': 'green', 'points': 5}
print(alien['color'])
new_points = alien['points']
print(f"You just earned {new_points} points.\n")

#You can also add new key-value pairs
print(alien)
alien['xpos'] = 0
alien['ypos'] = 50
print(alien)

#You can also start with an empty dictionary
alien2 = {}
alien2['color'] = 'green'
alien2['points'] = 5
print(alien2)
print("\n")

#You can also midify value in a dictionary
alien3 = {'color': 'green', 'points': 5}
print(alien3)
alien3['color'] = 'yellow'
print(alien3)
print("\n")

#You can use this in more complicated examples
alien4 = {'xpos': 0, 'ypos': 25, 'speed': 'medium'}
#Preten like we are moving it to the right
#Determine how far to move it based on speed
if alien4['speed'] == 'slow':
	x_incriment = 1
elif alien4['speed'] == 'medium':
	x_incriment = 2
else:
	x_incriment = 3 	#This is a fast alien
#The new position should be the old position and the incriment
alien4['xpos'] = alien4['xpos'] + x_incriment
print(f"New position: {alien4['xpos']}\n")

#You may also want to remove key value pairs
#Use the del statment to remove old pairs
print(alien3)
del alien3['points']
print(alien3)
print("\n")

#Dictionary of similar objects
#Sometimes you want to store one type of info about the same topic
fav_lang = {
	'jen': 'python', #You can break a dictionary into several lines
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
language = fav_lang['sarah'].title() #Ask for what sarah answered
print(f"Sarah's fav language is {language}")

#Accessing values using get()
alien5 = {'color': 'green', 'speed': 'slow'}
#You can use the get() method to bring a value when a key dosent exist
point_value = alien5.get('points', 'No point value assigned.')

#If theres a chance a key you're looking for dosent exist, use get()


