import math

second = (int(input("Enter number of second: ")))
minute = second / 60
hour = minute / 60
day = hour / 24

print ("=======================")

print (second, "second = ", math.floor(day), "days", ";", math.floor(hour), "hours", ";", math.floor(minute), "minutes" )