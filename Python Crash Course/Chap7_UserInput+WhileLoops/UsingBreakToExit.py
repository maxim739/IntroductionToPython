#Somethimes you want to exit a while loop without continuting running the code
#IThen you use a brake statment
prompt = "Enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you want to end the program: "

while True:	#A loop which starts with while True: will run forever until it reaches a break statment
	city = input(prompt)

	if city == 'quit':
		break	
	else:
		print(f"I'd love to go see {city.title()}")
#You can also use a break statment on any loop
