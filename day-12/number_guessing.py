import number_asci
from random import randint

attempts = 0
print(number_asci.guess_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

random_number = randint(1, 100)

difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficult == "easy":
    attempts = 10
elif difficult == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
        print("Too high")
        print("Guess again")
        attempts -= 1
    elif guess < random_number:
        print("Too low")
        print("Guess again")
        attempts -= 1
    elif guess == random_number:
        print(f"You got it! The answer is {random_number}")
        attempts = 0

    if attempts == 0 and guess != random_number:
        print("You have run out of guesses. You lose")
