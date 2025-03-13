import random
import my_module  # My module

# use random module
number = random.randint(1, 100)
print(f"First random number: {number}")

# use variable from my module
print(f"This is imported fovourite number: {my_module.my_favourite_number}")

# generate random number (increase into 10)
random_number_0_to_1 = random.random() * 10

print(f"andom number 0 to 1 is: {random_number_0_to_1}")

# random float number from 1 to 10
random_float = random.uniform(1, 10)
print(f"random float number: {random_float}")

# simple game to choice heads or tails , based on randint number
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("heads or tails?: Heads")
else:
    print("heads or tails?: Teils")

# First list with output
first_list = ["Adam", "Milena", "Monika", "Rafal"]
for i in first_list:
    print(f"List output one by one: {i}")

# add new item to the list
add_to_list = input("What to add?\n ")
first_list.append(add_to_list)
print("Po dodaniu:")
for i in first_list:
    print(f"WYnik z listy {i}")
