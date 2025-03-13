# Tip calculator for a restaurant bill

def calculate(bill, tip, people):
    total = bill * (1 + (tip / 100))
    per_person = total / people
    return per_person


print("Welcome to the tip calculator!")
bill = float(input("What wass the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

print(f"Each person schould pay: ${calculate(bill, tip, people)}")