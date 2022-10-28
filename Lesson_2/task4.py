userNumber = int( input ("Enter your numbers: ") )

secondUserNumber = userNumber

factorial = 1 

while secondUserNumber > 1 :
        factorial = factorial * secondUserNumber
        secondUserNumber = secondUserNumber - 1

print (userNumber, "!", "=", factorial) 