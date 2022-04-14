#You can use if else statments to pass code when a condition is not met
age = 17
if age == 18:
	print("Age is 18")
else:
	print("Your age is not 18")

#If-Elif-Else chain
if age == 18:
	print("Age is 18")
elif age == 17:
	print("Age is 17")
else:
	print("Age is not 17 or 18")
#You can use as many elif statment blocks as you want

#Omitting the else block
#You can omit the else block if an elif statment is more clear
if age == 18:
	print("Age is 18")
elif age == 17:
	print("\nAge is 17")

#Testing for multiple conditions
toppings = ['Pepperoni', 'Cheese', 'Mushroom']
if 'Pepperoni' in toppings:
	print("\nAdding Pepperoni")		#This is printed because the first condition is met
elif 'Cheese' in toppings:
	print("Adding cheese")		#This is not met because the elif statement is skipped when if statement is correct
if 'Mushroom' in toppings:
	print("Adding Mushrooms")		#This is printed because it is another if statement
print("Finished making your pizza")

#In conclusion, when you only want one line of code use an if-elif-else block, otherwise use independent if statments