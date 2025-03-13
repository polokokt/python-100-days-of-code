import random

friends = ["Adam", "Maciej", "Anna", "Damian", "Weronika"]

# Option 1
print(f"Today {random.choice(friends)} pays according to option 1")

# Option 2
print((
    f"Todat {friends[random.randint(0, len(friends)-1)]} "
    f"pays accordin to option 2"
))
