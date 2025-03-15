"""
This is the first version of "simple" blackjack game.
The rules are easrier than in the real game. A has locked value into 11.
"""

import random

card_value = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def choice_cards(cards_list):
    cards_list.append(random.choice(list(card_value.keys())))
    # cards_list.append(random.choice(cards))
    return cards_list


def change_list_to_string(long_list):
    return ", ".join(map(str, long_list))


def sum_cards(player_cards):
    suma = 0
    for card in player_cards:
        suma += int(card_value[card])
    return suma


def compare(user_sum, computer_sum):
    if user_sum > 21:
        print("You Lose. Game over !!!")
    elif user_sum == 21 and computer_sum != 21:
        print("You Win. Congratulations !!!!")
    elif user_sum == 21 and computer_sum == 21:
        print("You Lose. Game over !!!")
    elif user_sum > computer_sum:
        print("You Win. Congratulations !!!!")
    elif user_sum == computer_sum:
        print("You Lose. Game over !!!")
    elif user_sum < computer_sum:
        if computer_sum > 21:
            print("You Win. Congratulations !!!!")
        else:
            print("You Lose. Game over !!!")


user_cards = []
computer_cards = []

choice_cards(user_cards)
choice_cards(computer_cards)
choice_cards(computer_cards)

new_card = True

while new_card:

    choice_cards(user_cards)

    user_sum = sum_cards(user_cards)
    computer_sum = sum_cards(computer_cards)
    print(
        f"Player cards: {change_list_to_string(user_cards)}; Summary: {user_sum}",
        f"\nComputer first card: {computer_cards[0]}",
    )

    if user_sum > 21 or (user_sum == 21 and (computer_sum != 21 or computer_sum == 21)):
        new_card = False
    else:
        HS = input(
            "Choice Hit (h) to take another card," " or Stand (s) to check the cards: "
        )

        if HS == "h" ":":
            new_card = True
        elif HS == "s":
            new_card = False

while sum_cards(computer_cards) < 17:
    choice_cards(computer_cards)
    computer_sum = sum_cards(computer_cards)

print(
    "Summary:",
    "\nPlayer cards: " + f"{change_list_to_string(user_cards)}; Summary: {user_sum}",
    "\nComputer cards: "
    + f"{change_list_to_string(computer_cards)}; Summary: {computer_sum}",
)

compare(user_sum, computer_sum)
