#A function dosen't always display an output, sometimes it can return numbers or a set of values
def get_formatted_name(first_name, last_name):
	"""Return full name, neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('Jimi', 'hendrix')	#The value the fucntion returns is stored in musician instead of being printed out
print(musician)


#Making an argument optional
#Sometimes it makes sense to make an argument optional so that they can add extra information if they want
def get_formatter(first, last, middle=''):	#Have the middle name default as an empty string
	"""Format all three"""
	if middle:
		full = f"{first} {middle} {last}"
		return full.title()
	else:
		full = f"{first} {last}"
		return full.title()

print(get_formatter('John', 'Hooker', 'Lee'))
print(get_formatter('John', 'Hooker'))


#Returning a dictionary
#Python can return any dictionary you want, including a dictionary
#This code will take parts of a name and returns a dictionary representing a person
def build_person(first_name, last_name, age=None):
	"""Return a dictionary about a person"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
#Age = None, None is used when the variable has no specific value assigned to it, it acts as a placeholder value, and is false


#Using a function in a while loop
def get_formatted(first_name, last_name):
	"""Return full name, formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter q at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted(f_name, l_name)
	print(f"\nHello, {formatted_name}")
