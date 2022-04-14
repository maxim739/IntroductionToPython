# This is a guess the number game
import random

print("Hello, what is your name?")
name = input()
secretNum = random.randint(1, 20)
print(f"Hello {name} are you ready to play a game?\nTry and guess the number I'm thinking about")
guessesTaken = 0

while guessesTaken <= 6:
	guess = int(input("Take a guess for my number."))

	if guess == secretNum:
		print(f"You won the game with {guessesTaken} guesses! The number was {secretNum}.")
		break
	elif guess > secretNum:
		print("Your guess was too high! Guess again.")
		guessesTaken += 1
	elif guess < secretNum:
		print("Your guess was too low! Guess again.")
		guessesTaken += 1

print(f"You lost the game! The number was {secretNum}, sorry!")