#Checking for Special Items
toppings = ['mushrooms', 'peppers', 'extra cheese']
for item in toppings:
	print(f"Adding requested topping {item}")

#You can use an if and for if the pizzeria runs out of peppers
for item in toppings:
	if item == 'peppers':
		print("Sorry we are out of peppers")
	else:
		print(f"Adding {item}")

#You may also want to check if a list is not empty
reqtoppings = [] 	#Here you start with an epty list
if reqtoppings:		#If there are items in list, then if statment runs
	for item in reqtoppings:
		print(f"Adding {item}")
	print('Finished\n')
else:	#If there aren't any items in the list, then the else statment runs
	print("Are you sure you want an empty pizza?")

#You may also want to use two lists together and compare them
avaltoppings = ['mushrooms', 'peppers', 'extra cheese', 'olives', 'pineapple', 'pepperoni']
requtoppings = ['mushrooms', 'french fries', 'extra cheese'] #The above list could be a thuple if the toppings didnt change
for item in requtoppings:
	if item in avaltoppings:	#Loop to see if requested is a valid topping
		print(f"Adding {item}")	#Add topping if in avaliable toppings
	else:
		print(f"Sorry, we do not have {item}") #Dont add if they dont have it
print("Finished making your pizza\n")
