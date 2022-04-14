#Sometimes you won't know how many arguments you will need a function to pass, so python can collect an arbituary number of arguments
def make_pizza(*toppings):
	"""Print list of requested toppings"""
	print("\nMake a pizza with the following toppings: ")
	for topping in toppings:
		print(f"- {topping} ")

make_pizza('pepperoni')
make_pizza('mushrooms', 'tomato', 'extra cheese')
#The asterix in the parameter tells python to create an empty thuple which can take all the values put into it
#It is packed into a thuple even when there is only one argument


#Mixing positional and arbitrary arguments
#If you want a function to accept an arbitrary numbey of agreements, it must be placed last in the function definition
def pizza(size, *toppings):
	"""Summarize pizza about to make"""
	print(f"\nMake a {size}-inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"- {topping} ")

pizza(16, 'pepperoni')
pizza(24, 'mushrooms', 'extra cheese')

#You will often see the generic parameter '*args' which collects arbituary positional arguments like these


#Using arbituary keyword arguments
#Sometimes you want to accept an arbitruary amount of arguments, but you don't know what kind of information will be passed on
def build_profile(first, last, **user_info):
	"""Build a dict on everything we know of the user"""
	user_info['first name'] = first
	user_info['last name'] = last
	return user_info

user_profile = build_profile('albert', 'einstien', location='princeton', field='pysics')
print(user_profile)

#This expects a first and last name, but can pass as many key-value pairs that the user wants
#The double asterix causes python to build a dictionary called user_info
#Line 32-33 take information from the user
#The return takes any other arguments and directly insert them into the dictionary

#You will often see **kwargs used to collect non-specific keyword arguments