number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

operation = str(input("Enter the operation (+ ; - ; * ; /): "))

def functionResult ():
    if operation == "+":
        result = number1 + number2
    if operation == "-":
        result = number1 - number2
    if operation == "*":
        result = number1 * number2
    if operation == "/":
        result = number1 / number2
    return result


def consoleWrite ():
    print("Result: ",str(functionResult()))

consoleWrite()