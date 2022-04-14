#Using sort method premenantly makes the list alphabetically organized
cars = ['toyota', 'bmw', 'subaru', 'audi']
carsSort = cars
cars.sort()
print(cars)
#you can also make it sort reverse alphabetical order
reverseSort = cars
reverseSort.sort(reverse=True)
print(reverseSort)

#There is also the option to temporarily sort a list using sorted()
sortedCars = cars
print("\nHere is the OG list")
print(cars)
print("Here is the modified list")
print(sorted(sortedCars))
print("Heres the OG again")
print(sortedCars)

#Printing a list in reverse order using reverse()
reverseCar = cars
print("\n")
print(cars)
reverseCar.reverse()
print(reverseCar)

#You may also want to find the length of a list using len()
print("\n")
print(len(cars))
numCars = len(cars)
#you can use len in a string
print(f"We are suspecting {numCars} at the dealership")




