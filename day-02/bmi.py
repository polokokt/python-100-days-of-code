def bmi_calculate(height, weight):
    bmi = weight / (height ** 2)
    return bmi

print("This is BMI calculator!")

height = float(input("Enter your height as float: \n"))
weight = float(input("Enter your weight: \n"))

bmi = round(bmi_calculate(height, weight),2)

print(f"Your BMI is: {bmi}")
