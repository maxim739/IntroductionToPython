#Sometimes its useful to pass a list through a function, making lists more efficient
#Here is a list of people we want to greet, and we will greet them induvidually
def greet_users(names):
	"""Print greetign for users in the list"""
	for name in names:
		msg = f"Hello, {name.title()}"
		print(msg)

usernames = ['hanah', 'eric', 'ty']
greet_users(usernames)


#Modifying a list with a function
#When you pass a list throug ha function the changes are permenant, making data movement very efficient
#Here is an example where items that need to be printed are in a list, and after they are printed they are moved to another list
unprinted = ['phone case', 'robot', 'dice']
printed = []

while unprinted:
	current_design = unprinted.pop()
	print(f"Printing model: {current_design} ")
	printed.append(current_design)

print("\nThe following have been printed: ")
for complete in printed:
	print(complete)

#Here is the same code split into two functions
def print_models(unprinted, completed):
	"""Print each design, move to completed"""
	while unprinted:
		current = unprinted.pop()
		print(f"Printing model: {current_design} ")
		printed.append(current_design)

def show_completed(completed):
	"""Show all modeals that are printed"""
	print("\nThe following have been printed: ")
	for complete in printed:
		print(complete)

unprinted = ['phone case', 'robot', 'dice']
printed = []
print_models(unprinted, printed)
show_completed(printed)


#Preventing a function from modifying a list
#You can use this to make sure nothing happens to an origional list
#You can do this by sending the function a copy of the list, which can be done like:
#	function_name(list_name[:])
#The slice notation makes a copy of the list and sends that to the function
print_models(unprinted[:], printed)
#Now the values from the origional are passed on, but can't be removed from the origional list
print(printed)
print(unprinted)
