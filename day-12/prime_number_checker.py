# Program to check if the defined number is a prime number


def is_prime(num):
    results = []
    start_number = 1
    for i in range(1, num + 1):
        # while start_number <= num:
        if num % start_number == 0:
            results.append(num)
        start_number += 1
    if num == 1:
        return True
    elif len(results) == 2:
        return True
    else:
        return False


# Start the program
result = is_prime(75)
print(f"{result}")
