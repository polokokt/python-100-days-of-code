# This line of code will take an input string using input() function
print("Hello " + input("What is your name? ") + "!")

# input as variable
family_name = input("What is you family name? ")
print("Your family name is: " + family_name)
print("Family name length: " + str(len(family_name)))

# one line input and print function
print("String length: " + str(len(input("Input string to count length: "))))

# use variable for input and count lenght
username = input("Input second string to count length: ")
length = len(username)
print("String legth: " + username + " is: " + str(length))
