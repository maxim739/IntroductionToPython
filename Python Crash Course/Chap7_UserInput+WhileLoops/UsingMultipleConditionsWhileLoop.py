#You will want to use this when there are multiple events which trigger the while loop to stop running, like when a character dies in a game
prompt = "Tell me something you want to be repeated to you:"
prompt += "\nEnter 'quit' when you want to end the program: "

active = True	#Set variable avtive to True so that the while loop would be running
while active:	#Will run as long as active = True
	message = input(prompt)

	if message == 'quit':	#If the user enters quit
		active = False		#Change active to False so that the program wont run
	else:			#Otehrwise just run the program as usual
		print(message)	