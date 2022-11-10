userList = input("Enter your numbers: ")

lst = userList.split(",")
lst = [int(x) for x in lst]
lst.sort()
print ("Your list: ", [int(x) for x in lst])

print ("=====================")

print ("Max number: ", lst [-1])
print ("Min number: ", lst [0])

print ("=====================")

lst.pop(-1)
lst.pop(0)

print ("Sum of all other numbers: ", sum(lst))  