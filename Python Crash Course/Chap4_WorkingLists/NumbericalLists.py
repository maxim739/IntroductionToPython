#Using the range() function
#The counting starts at the first # provided and ends one before the last # provided
for value in range(1,5):
	print(value)
print("\n")
#You can also pass range using one argument
for value in range(6):
	print(value)

#You can also make a list of numbers using range
numbers = list(range(1,6))
print(numbers)

#The range function can also be used to skip numbers in a sequence
#Python uses the third value given as a step size
even_nums = list(range(2, 11, 2))
print(even_nums)

#You can create almost any set of numbers you want with range
squares = []
for value in range(1, 11):
	square = value ** 2		#You can also replace the indented code with 
	squares.append(square)	#squares.append(value**2)
print(squares)
print("\n")

#Simple statistics can also be done with python lists
digits = list(range(0,11))
print(min(digits))
print(max(digits))
print(sum(digits))