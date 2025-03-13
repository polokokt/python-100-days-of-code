programming_dictionary = {
    "Bug": "An error in a program..",
    "Function": "A piece of code...",
}

print(programming_dictionary["Bug"])

loop = input("Input the description for Loop: \n")

programming_dictionary["Loop"] = loop

print(programming_dictionary)

# Wipe an existing dictionary

# programming_dictionary = {}

# print(programming_dictionary)

# Loop for the dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
