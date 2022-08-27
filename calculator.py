from clear import clear

#Calculator functions
def add(n1, n2):
    """Adds the numbers together"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts second number from first"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divides first number into second"""
    return n1 / n2

def modulo(n1, n2):
    """Gets reminder from dividing first number into second"""
    return n1 % n2

def power(n1, n2):
    """Raises the first number by the power of second number"""
    return n1 ** n2

def floor(n1, n2):
    """Floor divides the first number by the second number"""
    return n1 // n2

#Library of functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": power,
    "//": floor
}


def calculator():
    print(logo)
    #Inputs
    num1 = float(input("First number: "))
    for key in operations:
        print(key)
    
    #Looping
    go_again = True
    while go_again:
        operation_style = input("Pick an operation method: ")
        num2 = float(input("Next number: "))
        calc_function = operations[operation_style]
        answer = calc_function(num1, num2) 
        print(f"\n{num1} {operation_style} {num2} = {answer}\n")
        
        again_check = input(f"Continue with {answer}? Y/N").lower()
    
        #Again exit/continue
        if not again_check == "y" and not again_check == "n":
            print("Invalid input.")
            again_check = input(f"Continue with {answer}? Y/N ").lower()
        elif again_check == "y":
            go_again = True    
            num1 = answer
            print(num1)
        elif again_check == "n":
            go_again = False
            clear()
            calculator()

calculator()
