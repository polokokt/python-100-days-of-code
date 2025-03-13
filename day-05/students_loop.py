student_scores = [
    87,
    125,
    133,
    98,
    176,
    59,
    112,
    162,
    134,
    78,
    186,
    83,
    91,
    177,
    142,
    150,
    93,
    61,
    193,
    171,
    72,
    118,
    155,
    80,
    107,
    137,
    167,
    139,
    66,
    120,
    160,
    145,
    73,
    88,
    129,
]

# function sum
print(f"Summary students scores: {sum(student_scores)}")

# count sum in the loop

total = 0

for score in student_scores:
    total += score

print(f"Sum from the loop: {total}")

# build in max function

print(f"Max value based on max function: {max(student_scores)}")

# max value achieved from loop

max = 0

for number in student_scores:
    if number > max:
        max = number

print(f"Max score from the loop: {max}")
