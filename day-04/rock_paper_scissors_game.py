import random
import rps_game_module

your_input = int(input("What do you choose. 0 for rock, 1 for scissors, 2 for papper:\n "))

computer_int = random.randint(0, 2)
list_of_elements = [
    rps_game_module.rock,
    rps_game_module.scissors,
    rps_game_module.paper,
]
print(f"Computer choiced: {computer_int}")

print("You choiced:\n")
print(list_of_elements[int(your_input)])
print("Computer choiced:\n")
print(list_of_elements[int(computer_int)])


if your_input == 0:
    if computer_int == 0:
        print("Nobody win")
    elif computer_int == 1:
        print("You win")
    else:
        print("Computer win")
elif your_input == 1:
    if computer_int == 0:
        print("Computer win")
    elif computer_int == 1:
        print("Nobody win")
    else:
        print("You win")
elif your_input == 2:
    if computer_int == 0:
        print("You win")
    elif computer_int == 1:
        print("Computer win")
    else:
        print("Nobody win")
else:
    print("Wrong number !!!")
