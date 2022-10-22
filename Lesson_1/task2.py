firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
print ("========================")
operation = str(input("Choose an operation: "))
print ("========================")

if operation == "+" :
    r = firstNumber + secondNumber
if operation == "-" :
    r = firstNumber - secondNumber
if operation == "/" :
    r = firstNumber / secondNumber
if operation == "*" :
    r = firstNumber * secondNumber

print ("Result: ",r )
