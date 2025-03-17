# Higher or Lower - a game where the player must guess which person
# or item has a higher number of searches, followers, or another comparative value.
# The goal is to keep selecting the option with the higher
# value and continue the streak for as long as possible.

import game_data
import random
import os

game_data_length = int(len(game_data.data))


def random_data():
    data_a = random.randint(0, game_data_length - 1)
    data_b = random.randint(0, game_data_length - 1)
    while data_a == data_b:
        data_b = random.randint(0, game_data_length - 1)

    print(
        f"Compare A: {game_data.data[data_a]['name']}, {game_data.data[data_a]['country']}, {game_data.data[data_a]['description']}"
    )
    print(
        f"Against B: {game_data.data[data_b]['name']}, {game_data.data[data_b]['country']}, {game_data.data[data_b]['description']}"
    )

    return data_a, data_b


def check_result(random_a, random_b, answer):
    score_a = int(game_data.data[random_a]["follower_count"])
    score_b = int(game_data.data[random_b]["follower_count"])

    who_win = ""

    if score_a > score_b:
        who_win = "A"
    else:
        who_win = "B"

    if who_win == answer:
        return True
    else:
        return False


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def game():
    player_win = True
    score = 0
    while player_win:
        clear_screen()
        if score > 0:
            print(f"You have right. Your score: {score}")
        a, b = random_data()
        answer = input("Who has more followers? Type 'A' 'or 'B': ")
        player_win = check_result(a, b, answer)
        if player_win == True:
            score += 1
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {score}")


game()
