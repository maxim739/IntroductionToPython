#This if test tests if a car is bmw then it will display in all uppercase, but the others are in title case
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#Conditional Tests
#A conditional test is a test which has a condition to be True or False
#Python uses True and False values to decide if a code should be written
car == 'bmw'	#This line checks whether the value of car is 'bmw'
car = 'bmw'		#This line set the variable car equal to 'bmw'
#conditionals are also case sensitive
car.lower() == 'Audi'	#This is True because Audi turns into audi
car == 'Audi'			#This is not True because Audi is not an item in the list

#Checking for inequality
#If you want to determine if two values are not equal you can use !=
requested_topping = ['mushrooms']
if requested_topping != 'anchovies':
	print("Hold the anchovies")
#Python tests if the requested topping is anchovies, and if it isn't, then it is told to not add anchovies

#Numberical Comparisons
age = 18
age == 18	#Testing numerical values is pretty straighforward
#You can also use them in if tests
answer = 17
if answer != 42:
	print("That is not the correct answer!")
#You can also have various mathamatical comparisons as conditions
age > 12	#True
age < 20	#True
age <= 20 	#True
age >= 20 	#False

#Checking Multiple Conditions
#To check two conditions, use keywords
#And is used to combine two conditional tests
age_1 = 22
if age_1 >= 20 and age >= 21: 	#Here you test if 22 is greater than 20, and if 18 is greater than 20
	print("False")				#Because one of those conditions is not true, 
else:							#then the if statement dosen't excecute
	print("True")
#You can also use or to check multiple conditions
#Use or to pass when one or both conditions pass
num = 10
num1 = 15
if num >= 9 or num1 == 15:
	print("This is True")

#Checking whether a value is in a list
#Sometimes you want to check if a value is already in a list before action
toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in toppings:
	print("\nYes")
if 'cheese' not in toppings:
	print("Cheese is not in the pizza")

#You can also check if a value is not in a list
if 'peppers' not in toppings:
	print("Peppers are not in toppings")

