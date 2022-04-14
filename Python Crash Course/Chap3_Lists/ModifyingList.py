motorcycles = ['honda', 'yamaha', 'suzuki', 'KTM', 'Cafe Bike']
print(motorcycles)
#You can change the items in a list by changign their "value"
motorcycles[0] = 'ducati'
print(motorcycles)

#You can also add elements to a list
#Using append to add to the back of the list, without affecting the others
motorcycles.append('honda')
print(motorcycles)
#You can also append to empty strings
bikes = []
bikes.append('Marin')
bikes.append('Santa Cruz')
print(bikes)

#You can also insert elements into a list
#insert() makes a space and then inserts the new value in that space
bikes.insert(1, 'Treck')
print(bikes)

#You can remove an item from a list
#Using the del statment you can use indexes
del bikes[2]
print(bikes)

#You can also use the pop() method
#Using the pop method you can use the value of something that is being deleted from a list
#Like to move a value from one area to another, etc.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#pop() works on the last item of a list, and will print not inside a list to show that the deleted value si now assigned to the new variable
#look at pg 40 in book
last_owned = popped_motorcycle
print(f"The last motorcycle I bought was a {last_owned.title()}.")
#You can also pop() any item in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I bought was a {first_owned.title()}")

#You can also remove an item based on value when you dont know what index it has
#Using the remove() method
motorbike = ['honda', 'yamaha', 'suzuki', 'ducati']
motorbike.remove('ducati')
print(motorbike)
#you can use this method to work with a value being removed from a list
too_expensive = 'honda'
motorbike.remove(too_expensive)
print(motorbike)
print(f"\nA {too_expensive.title()} was too expensive for me.")
#remove only works for the first instance it comes across, so to get rid of multiple of the same value
#in a list, you will need to use a loop