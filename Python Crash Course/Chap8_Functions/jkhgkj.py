unprinted = ['phone case', 'robot', 'dice']
printed = []

def print_models(unprinted, completed):
	"""Print each design, move to completed"""
	while unprinted:
		current = unprinted.pop()
		print(f"Printing model: {current} ")
		printed.append(current)

def show_completed(completed):
	"""Show all modeals that are printed"""
	print("\nThe following have been printed: ")
	for complete in printed:
		print(complete)

print_models(unprinted, printed)
show_completed(printed)