#Slicing a list
#To slice a list you specify the index of the first function and the last elemets you want to work with
players = ['Charles', 'Martins', 'Michael', 'Florence', 'eli']
print(players[0:3])
print(players[1:4])
#If you omit the first index in a slice, it automatically starts at the front
print(players[:4])	#This one starts at the neginning and ends at 4
#This also works in the opposite
#This syntax allows you to output all the elements of a list regardless of where it starts
print(players[2:])	#This slice starts at 2, and ends at the end of the list
#You can also use negative indexes to return an element a certain distance from the end
print(players[-3:])	#This slice prints the last three elements of the list
#You can also include a third value, which tells python which elements to skip in the specified range
print(players[1:4:2])	#This slice skips the middle value in the slice

print("\n")

#You can also loop through a slice
#You use a for loop to loop through the elements in a slice
print("There are three players on my team.")
for player in players[:3]:
	print(player.title())