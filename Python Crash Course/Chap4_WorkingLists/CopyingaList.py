#Here we have a list of favorite foods, and also a list of our friend's which is identical
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My fav foods are:")
print(my_foods)

print("\nMy friend's fav foods are:")
print(friend_foods)

#If you set two lists equal without a slice format at the end "[:]"
#They would not produce two seperate lists
#Instead python would associate the two lists as the same, and not seperate
