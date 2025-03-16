# Global variable

enemies = 1

# Global Constants
PI_NUMBER = 3.14159
GOOGLE_URL = "https://www.google.com"


def increase_enemies():
    enemies = 2
    print(f"Number of enemies: {enemies} in local scope")


increase_enemies()
print(f"Number of enemies: {enemies} in global scope")

# Proper modification of global scope variable

horses = 1


def increase_horse(horse):
    print("Adding 1 horse to the hord of horses")
    return horse + 1


print(f"Horses before increase: {horses}")
horses = increase_horse(horses)
print(f"Horses after increase: {horses}")


# Print/Use global constatns
def my_func():
    print(PI_NUMBER)


my_func()
