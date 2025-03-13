"""
You are going to write a program that automatically prints
the solution to the FizzBuzz game.

These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100, including 100.
- If a number is divisible by 3, print "Fizz" instead of the number.
- If a number is divisible by 5, print "Buzz" instead of the number.
- If a number is divisible by both 3 and 5 (e.g., 15), print "FizzBuzz".
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
