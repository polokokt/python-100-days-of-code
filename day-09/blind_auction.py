import art

print(art.logo)


def find_the_winner(list_of_bidders):
    winner = ""
    price = 0
    for name in list_of_bidders:
        if int(list_of_bidders[name]) > price:
            price = int(list_of_bidders[name])
            winner = name
    print(f"The winner is {winner} with a bid of ${price}")


print("Welcome to the secret auction program.")

next_person = True
name = ""
bid = 0
bidders = {}

while next_person:
    name = input("What is your name?: ")
    bid = input("What is your bid?: ")
    bidders[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no'.") == "no":
        next_person = False
        print("\n" * 100)
        find_the_winner(bidders)
    else:
        print("\n" * 100)
