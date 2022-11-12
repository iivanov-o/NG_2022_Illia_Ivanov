userStroke = input ("Enter your stroke: ")
alphabet = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
userStroke = list(userStroke)
userStroke.sort()
print (userStroke)
for (letter) in userStroke:
    count = userStroke.count (letter)
    if letter == alphabet:
        letter = letter + 1
    if letter == ' ':
        count = 0
    if count > 0: 
        lst = letter, "-", str(count)
        lst = ' '.join(lst)
        print (lst, end = "; ")