# Enter the number. I will check if this is even number

def check(number):
    if number % 2 == 0:
        print("This is even number")
    else:
        print("This is not even number")

number_to_check = int(input("Input your number"))

check(number_to_check)

