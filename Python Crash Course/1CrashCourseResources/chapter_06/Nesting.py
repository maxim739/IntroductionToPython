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

for alien in alienx[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for x in alienx[:5]:	#In this loop we go through the list aliens and slice the first 5
	print(x)			#Then we print the first five items in aliens
print("...")

print(f"total number of aliens: {len(alienx)}"