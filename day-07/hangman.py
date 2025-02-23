import random
import blanks_generator
import hangman_asci

words_list=["parasol", "torba", "lina", "krokodyl", "ryba"]

chosen_word = random.choice(words_list)
# print(chosen_word)

placeholder = blanks_generator.generate(chosen_word)
print(placeholder)

display = placeholder
correct_letters = []    # list to keep correct letters guess by the gamer
counter = -1            # counter of lives (reverse)
while "_" in display:
    guess = input("What is your letter?:\n ").lower()
    if guess not in correct_letters:
        if guess in chosen_word:
            display = ""
            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    correct_letters.append(letter)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"

            if counter >= 0:
                counter -= 1
                if counter > -1:
                    print(hangman_asci.HANGMANPICS[counter])
        else:
            counter += 1
            if counter == 6:
                print(hangman_asci.HANGMANPICS[counter])
                print("You LOOSE !!!!")
                exit(0)
            else:
                print(hangman_asci.HANGMANPICS[counter])
        print(display)
        # print(counter)
        if "_" not in display:
            print("You WIN !!!!")