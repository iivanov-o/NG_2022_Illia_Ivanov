userList = input ("Enter your numbers: ")
print ("=========================")
print ("Your list: ", list(userList.split(",")))

print ("=========================")

secondList = list(set(userList.split(",")))

secondList.sort()

print ("Your list with unique numbers: ", secondList)