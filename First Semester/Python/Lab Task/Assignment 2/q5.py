"""Write a function that computes hypotenuse of a right angled triangle by following the steps given  below. Hypotenuse2 = Base2 + Perpendicular2

a) Take base and perpendicular as inputs.
b) Create a function calculateSquare() for calculating and returning square of a number.
c) Create a function calculateHypotenuse() for calculating hypotenuse of a right angle triangle. Make use of the calculateSquare() function.
"""

import math
def calculateSquare(num):
    return num ** 2

def calculateHypotenuse(base, perpendicular):
    hypotenuse_squared = calculateSquare(base) + calculateSquare(perpendicular)
    hypotenuse = math.sqrt(hypotenuse_squared)
    return hypotenuse

base = float(input("Enter the base of the triangle: "))
perpendicular = float(input("Enter the perpendicular of the triangle: "))

hypotenuse = calculateHypotenuse(base, perpendicular)
print(f"The hypotenuse of the triangle is: {hypotenuse}")