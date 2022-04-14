#Lists work well for storing items which can change throughout a program
#But thuples create a list which cannot change
#A thuple is an immutable list
dimensions = (500, 50)	#The same syntax as a list, excpet with parenthesis
print(dimensions[1])	#You can also use indexing in the same way
#If you try and change the value of a thuple item like going
#dimensions[1] = 60 -> it will return an error
#Thuples are actually defined by commas, so if you want to create a thuple with one item
#You need to have it be like 
dime = 3,
dim = (3,) #Thuples need to have a trailing comma
print(dime[0])
print(dim[0])

print("\n")

#Looping through all the values in a thuple
for dimension in dimensions:
	print(dimension)

#You can also write over a thuple, while you cant modify one
print("Origional Dimensions:")
for val in dimensions:
	print(val)

dimensions = (400, 100)
print("\nModified Dimensions:")
for val in dimensions:
	print(val)
