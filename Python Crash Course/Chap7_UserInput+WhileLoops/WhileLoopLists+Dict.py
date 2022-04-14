#Moving items from one list to another
#Have an empty list and a full list
unconfirmed = ['alice', 'brian', 'candace'] 	#Here is a list of unconfirmed users
confirmed = []	#Here is a list of confirmed users

while unconfirmed:	#This loop runs as long as there are unconfirmed users
	current_user = unconfirmed.pop()	#The pop() method removes unverified users one at a time from the end of the list

	print(f"Verifying user: {current_user.title()}")
	confirmed.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed:
	print(confirmed_user.title())


#Removing all instances of specific values from a list
#You can use this to remove all instances of a specified value from a list
pets = ['dogs', 'cat', 'dog', 'goldfish', 'cat', 'cat', 'rabbit']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)


#Filling a dictionary with user input
#You can get as much info as you want with a while loop, here we are going to make a polling program
responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name?")	#Here the user is prompted for their name and what mountain they would like to climb
	response = input("Which mountain would you like to climb someday?")

	responses[name] = response 	#This is where the information is stored in the responses dictionary

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':		#The user is asked if they would like to keep the poll running or not
		polling_active = False

print("\n---Poll Results---")
for name, response in responses.items():	#This block prints the results of the poll per item in responses
	print(f"{name} would like to climb {response}. ")