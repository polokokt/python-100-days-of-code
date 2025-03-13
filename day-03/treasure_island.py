print("Welcome to Treasury Island game!")
print("Your mission is to find the treasure.")

if (
    input(
        'You are on the cross road. Where you want to go?\n        Type "left" or "right"\n'
    ).lower()
    == "left"
):
    if (
        input(
            'Do you want to swim over the lake or wait?\n        Type "wait" or "swim"\n'
        ).lower()
        == "wait"
    ):
        doors = (
            input(
                'You found a house with three dors. Which doors you choice?\n        Type "blue", "red" or "yellow"\n'
            ).lower()
            == "yellow"
        )
        if doors == "yellow":
            print("You win! You found the treasure !")
        elif doors == "red" or doors == "blue":
            print("Wrong door. Game over !!! :( ")
        else:
            print(". The door in such color doesn't exist. Game over !!! :( ")
    else:
        print("The crocodile ate you for dinner. Game over. !!! :( ")
else:
    print("Game over !!! :( ")
