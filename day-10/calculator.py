def adding(n1, n2):
    return n1 + n2
def subtracting(n1, n2):
    return n1 - n2
def multiplying(n1, n2):
    return n1 * n2
def dividing(n1, n2):
    return n1 / n2

operations = {
    "+": adding,
    "-": subtracting, 
    "*": multiplying,
    "/": dividing,
}

another_count = True
continus = False
operation_result = 0

while another_count:
    if continus == False:
        first_number = float(input("What is the first number?: "))
    else:
        first_number = operation_result

    for oper in operations:
        print(oper)

    operator = input("Pick an operation: ")

    second_number = float(input("What is the second number: "))

    ## the main operation. Take the operation from the input and put it into dictionary. This points into proper def and we can add numbers like function call
    
    operation_result = operations[operator](first_number, second_number)

    print(f"Operation result is: {first_number} {operator} {second_number} = {operation_result}")

    question = input(f"Type 'y' to continue calculating with $operation_result, or type 'n' to start a new calculation: ")
    if question == "y":
        continus = True
    elif question == "n":
        continus = False

