def life_in_weeks(age):
    weeks = (90 - int(age))*52
    return weeks

age = input("How old are you?\n ")

print(f"You have {life_in_weeks(age)} weeks left")