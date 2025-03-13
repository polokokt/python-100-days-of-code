# BMI calculator with interpetation (if/else)

weight = float(input("Enter your weight:\n "))
height = float(input("Enter your height:\n "))

bmi = weight / (height**2)

if bmi < 18.5:
    print(f"Your weight is underweight with bmi = {bmi}")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your weight is normal with bmi = {bmi}")
else:
    print(f"Your weight is overweight with bmi = {bmi}")
