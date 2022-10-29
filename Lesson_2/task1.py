userList = input("Enter your numbers: ")

lst = userList.split(",")
lst.sort()
print ("Your list: ", lst)

print ("=====================")

print ("Max number: ", lst [-1])
print ("Min number: ", lst [0])

print ("=====================")