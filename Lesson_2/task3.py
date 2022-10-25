userNumber = int(input(("Enter your number: ")))


while userNumber > 0:
    secondNumber = userNumber

    while secondNumber > 0:
        print (secondNumber, end='')
        secondNumber = secondNumber - 1
    
    userNumber = userNumber - 1
    print (" ")
    


