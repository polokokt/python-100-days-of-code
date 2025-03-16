from random import randint
import number_asci

# Global constant

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check users' guess against actual answer


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high!")
        # Track the number of turns and reduce by 1 if wrong
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it. The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(number_asci.guess_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Choosing a random number between 1 and 100

    answer = randint(1, 100)

    turns = set_difficulty()

    # Let user guess the number
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses. You lose")
            return
        if guess != answer:
            print("Guess again")


game()
