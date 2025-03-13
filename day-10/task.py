def format_name(f_name, l_name):
    if f_name =="" or l_name == "":
        return "You didn't privide valid inputs"
    formated_name = f_name.title()
    formated_lastname = l_name.title()

    return f"{formated_name} {formated_lastname}"

name = input("Write name: \n")
lastname = input("Write lastname: \n")

print (format_name(name, lastname))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print (function_2(function_1("hello")))
    
    