import cesar_asci

print(cesar_asci.CESAR_LOGO)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

while should_continue == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt message:\n ")
    text = input("Type your message:\n ")
    shift = int(input("Type the shift number:\n "))

    def cesar(text_to_cesar, shift_ammount, direction):
        cesar_text = ""

        if direction == "decode":
            shift_ammount *= -1

        for letter in text_to_cesar:
            if letter.isalpha():

                shifted_position = alphabet.index(letter) + shift_ammount
                shifted_position %= len(alphabet)
                cesar_text += alphabet[shifted_position]
            else:
                cesar_text += letter
        print(f"Cesar {direction} text: {cesar_text}")

    cesar(text, shift, direction)
    what_next = input("Do you want input another text? (Yes/No):\n ")
    if what_next == "Yes":
        should_continue = True
    else:
        should_continue = False