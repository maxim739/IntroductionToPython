#How the input() function works
#Input() pauses the program to wait for a user response, and then assigns the reponse to a variable
message = input("Tell me something to repeat:")
print(message)

#Make sure the input you are asking for is clear to understand
name = input("Please enter your name: ")
print(f"Hello {name}!")

#Making prompts bigger than one line
prompt = "Here is a prompt that is bigger than one line which is asking you for information"
prompt += "\nWhat is your name?"
name = input(prompt)
print(name)
#The first line assigns a string to a variable, and the second adds more string to the same variable

#You can use int() to accept numberical input
#When the input() function is used, it is stored as a string, but you can use it as a intiger if you use int()
age = input("How old are you?")
print(age)  #You cant use comparisons on this one because it is a string, so it would be like comparing letters
age = int(age)  #This line turns a string into an intiger
print(age)  #You can now compare this number to others because it is a number

#Here is an aexample for a rollercoaster
height = input("How tall are you in inches?")
height = int(height)

if height >= 48:
    print("\nYou are tall enogh to ride!")
else:
    print("\nYou are not tall enough to ride")

#Modullo operators
#These return the remainder of a division equation, instead of how many times a number fits into another
print(5 % 3)    #This equals 2
#You can use this function to determine if a number is even or odd
num = input("Enter a number, and I'll tell you if it;s even or odd:")
num = int(num)

if num % 2 == 0:
    print(f"\nThe number {num} is even")
else:
    print(f"\nThe number {num} is odd")
