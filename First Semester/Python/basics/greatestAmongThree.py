# WAP to calculate greatest among three numbers.

x = 10
y = 11
z = 10

if x == y == z:
    print("All numbers are equal")
elif x >= y and x >= z:
    print("x is the greatest")
elif y >= x and y >= z:
    print("y is the greatest")
else:
    print("z is the greatest")