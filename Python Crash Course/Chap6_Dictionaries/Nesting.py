#Nesting is when you want to store multiple dictionaries in a list or multiple lists in a dictionary
alien0 = {'color': 'green', 'points': 5}
alien1= {'color': 'yellow', 'points': 10} 	#First create the dictionaries
alien2 = {'color': 'red', 'points': 15}

alien = [alien0, alien1, alien2] 	#then store the dictionaries in a list called alien
for x in alien:	#Loop through and print out each alien
	print(x) 
print("\n")
#Here is another more practical example
aliens = [] 	#make an empty list

for alien_num in range(30):		#Here we make 30 green aliens
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for x in aliens[:5]:	#In this loop we go through the list aliens and slice the first 5
	print(x)			#Then we print the first five items in aliens
print("...")

print(f"total number of aliens: {len(aliens)} \n")	#This line shows how many items are in the list aliens, and prints it
#Even if all these aliens are the same, python considers them different objects, which allows us to modify them induvidually
#If you want to adress them induvidually, you can, which you would do in a game

alienx = [] 	#make an empty list

for alien_num in range(30):		#Here we make 30 green aliens
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	alienx.append(new_alien)

for alien in alienx[:3]:		#Here we only identify the first three items in the list
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for x in alienx[:5]:	
	print(x)			
print("...")
print(f"total number of aliens: {len(alienx)}")
print("\n")
#In this previous code is the same as the one before it, except we identify the first three items and change
#Their values
#You can also use elif statments
#Here it is without rewriting the whole block of code
#for alien in aliens[0:3]:
	#if alien['color'] == 'green':
		#alien['color'] = 'yellow'
		#alien['speed'] = 'medium'
		#alien['points'] = 10
	#elif alien['color'] == 'yellow':
		#alien['color'] = 'red'
		#alien['speed'] = 'fast'
		#alien['points'] = 15


#Here is a list in a dictionary
#A list in a dictionary is helpful when there are multiple aspects you might want to decribe
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese']
	}
print(f"You ordered a {pizza['crust']}-crusted pizza "
	"with the following topppings:")
for topping in pizza['toppings']:
	print(f"\t{topping}")
#You can insert a list in a dictionary as a value in a key value pair when you want more
#than one value to be associated with a key. 

fav_lang = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in fav_lang.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
#To refine this code you would refine it to check if there is only one language, and change the code accordingly

#You can also store dictionaries in dictionaries, but this has potential to get complicated quickly
#Here we use a dictrionary to store someones username, and then that username hold different values in it as well
users = {
	'aeinstien': {
		'first': 'albert',
		'last': 'einstien',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
#The structure of the dictionaries make the most sense to a reader, and they are more organized to acess (more intuitive)
