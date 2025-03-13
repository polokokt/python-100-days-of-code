def count(year):
    """Check if it is leap year"""
    leap_year = "True"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = "True"
            else:
                leap_year = "False"
        else:
            leap_year = "True"
    else:
        leap_year = "False"
    return f"{leap_year}"

print(count(int(input("Tell my the year: \n"))))



