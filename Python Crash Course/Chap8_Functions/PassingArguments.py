#There are many ways to pass an argument with multiple parameters
#One way is to have arguments in the same order they are written
#Another way is to do a keyword argument, which each argumaent is a variable and value, and lists and dictionaries of values

#Positional arguments
def describe_pet(animal_type, pet_name):
	"""Display Info about the pet."""
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')

#Multiple function calls
#To call the function again, you just need another line with the same info fomratting as the first in line 11
describe_pet('dog', 'willie')
#Order matters in positional arguments, as changing the order switches the values of the variables


#Keyword arguments
#This is a name-value pair used to pass a function. You directly associate the name and value within the argument
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')	#Remember to use exact names of parameters in the function's definition


#Default Values
#You define a default value for each parameter
#If an argument is provided for a value, python uses it, otherwise it will use a default value
def des_pet(pet_nme, ani_type='dog'):
	"""Display more info abt pet"""
	print(f"\nI have a {ani_type}")
	print(f"My {ani_type}'s name is {pet_nme.title()}")

des_pet(pet_nme='willie')
#Now the dafault value for animal type is dog, so if that argument is not given, it is dog
#There is an even more simple way to call this function
des_pet('willie')
#This can also be overwritten and used as normal
des_pet(pet_nme='harry', ani_type='hamster')


#Equivalent Function Calls
#There are many ways to call the same function, either the positional or keyword method


#Avoid argument errors
#Make sure argument names are spelled right
