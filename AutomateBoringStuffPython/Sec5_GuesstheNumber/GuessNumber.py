# This is a guess the number game
import random

print("Hello, what is your name?")
name = input()

print(f"Hello {name} are you ready to play a game?\nTry and guess the number I'm thinking about")
secretNum = random.randint(1, 20)

for guessesTaken in range(1, 7):
    guess = int(input("Take a guess. "))

    if guess < secretNum:
        print("Your guess is too low")
    elif guess > secretNum:
        print("Your guess is too high")
    else:
        break   # Only breaks if its the correct guess

if guess == secretNum:
    print(f"Good job {name}! You guessed my secret num in {guessesTaken} guesses")
else:
    print(f"Nope. The number I was thinking of was {secretNum}")