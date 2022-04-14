#You will want to store data in order to save user prefrences and inputs
#When users close the program, the data saved in dictionaries and lists must be saved, which is when we use the json module

#This module allows you to dump simple structures like lists and dictionaries into a file and load that file when the program is ran again
#You can also use json to share data between two different programs
#The json format is also not specific to python, so you could share data with another programming language
	#Json stands for Javascript Object Notation


#Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'json_files/numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)
#we import json and make a list of numbers, and then json.dump() is used to store the list
#The json.dump() function takes two arguments, the piece of data to store, and the file object used to store the data


#Here is how we will open the json file and use the list
with open(filename) as f:	#Here we open the file in read mode
	numbers = json.load(f)	#Here we use the json.load() function to load the info stored in the file and assign it to a variable

print(numbers)



#Saving and reading user generated data
#Using json is useful for storing user information, which would otherwise get lost when the program ends
#With json files that data can be saved and accessed later
username = input("What is your name? ")		#Here we prompt the username for store

filename1 = 'json_files/username.json'		
with open(filename1, 'w') as f:				#Here we use json.dump(username, f) passing it a username and a file object to store it in a file
	json.dump(username, f)		
	print(f"We'll remember your name when you come back {username}. ")

#In this next area of code we will greet a username who's username has already been stored
filename2 = 'json_files/username.json'
with open(filename2) as f:
	username = json.load(f)		#Here we load the information stored in username.json and assign it to the variable username
	print(f"Welcome back {username}! ")	#Here we use that new stored variable to welcome back the user


#Here we can combine the two into one block of code so that someone can retrive their memorized username if possible, and can create a username if they dont have one
#Load the username if it has been stored previously
#Otherwise prompt for a username and store it
filename3 = 'json_files/username1.json'

try:
	with open(filename3) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename3, 'w') as f:
		json.dump(username, f)
		print(f"We will remember you when you come back {username}. ")
else:
	print(f"Welcome back, {username}! ")

#Once you run this code once without changing or creating a new json file, the code will pass without a name prompt because the username is remembered
	#This will print the "welcome back again {username}. " line


#Refactoring
#Refactoring is when you see that your code works, but you can streamline it so that it works better by splitting it into different functions
#The greeting the user can be made into a function
def greet_user():
	"""Greet user by name"""
	filename4 = 'json_files/username2.json'

	try:
		with open(filename4) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename4, 'w') as f:
			json.dump(username, f)
			print(f"We will remember you when you come back {username}. ")
	else:
		print(f"Welcome back, {username}! ")
 
 greet_user()

 #Because this is in a function we can describe it with a docstring and make it much cleaner
 #However it is doing a lot and the docstring does not accuratley describe it, so we can refactor some more
 def get_stored_username():
 	"""Get stored name if avaliable"""
 	filename5 = 'json_files/username3.json'
 	try:
 		with open(filename5) as f:
 			username = json.load(f)
 	except FileNotFoundError:
 		None
 	else:
 		return username

def get_new_username():
	"""Prompt for a new usernam"""
	username = input("What is your name? ")
	filename6 = 'json_files/username4.json'
 		with open(filename6, 'w') as f:
 			json.dump(username, f)
 	return username


 def greet_user1():
 	"""Greet user by name"""
 	username = get_stored_username()
 	if username:
 		print(f"Welcome back to my crib {username}! ")
 	else:
 		username = get_new_username()
 		print(f"We'll remeber you when you come back, {username}! ")

greet_user1()