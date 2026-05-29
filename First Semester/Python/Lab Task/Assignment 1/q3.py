"""
Write a program to find root of the equation 4x**2 -21x + 25=0 using the formula
x = (-b ± √(b² - 4ac)) / 2a
"""
import math
a = 4
b = -21
c = 25

discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The roots are real and the same: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")