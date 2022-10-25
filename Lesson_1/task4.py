print ("Enter the coefficients for the equation")
print ("ax^2 + bx + c = 0")

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

print ("====================")

discriminant = b**2 - 4 * a * c

sqrt_discriminant = discriminant ** .5

if discriminant > 0 :
    x1 = ( -b + sqrt_discriminant ) / (2 * a)
    x2 = ( -b - sqrt_discriminant ) / (2 * a)
    print ("Solution: \nx1 =", x1, "\nx2 =", x2, ".")
elif discriminant == 0 :
    x = -b / 2 * a
    print ("Solution: \nx =", x, ".")
else:
    print ("There is no solution.")