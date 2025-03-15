import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")"]

length = input("How long you want the password should be?\n ")
symbols_to_use = input("How many symbols would you like to be in password?\n ")
numbers_to_use = input("How many numbers would you like to be in password?\n ")

random_symbols = random.sample(symbols, int(symbols_to_use))
random_numbers = random.sample(numbers, int(numbers_to_use))
random_letters = random.sample(letters, int(length) - int(symbols_to_use) - int(numbers_to_use))

new_password = random_symbols + random_numbers + random_letters
random.shuffle(new_password)

final_password = "".join(new_password)

print(f"Your new password: {final_password}")
