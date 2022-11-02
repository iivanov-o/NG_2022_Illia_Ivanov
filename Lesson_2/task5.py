userList = input("Enter your numbers: ")

lst = userList.split(",")
lst.sort()
print ("Your list: ", [int(x) for x in lst])

print ("=====================")

print ("Max number: ", max(lst))
print ("Min number: ", lst [0])

print ("=====================")

sumNumber = lst.pop(0)
sumNumber = lst.pop(-1)

lst = [int(x) for x in lst]

print ("Sum of all other numbers: ", sum(lst))