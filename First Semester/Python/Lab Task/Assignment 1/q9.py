"""
Write a program to repeatedly print the value of the variable num which is input by user. Value should be decreasing by 0.5 each time, as long as x Value remains positive.
"""
num = float(input("Enter a positive number: "))
while num > 0:
    print(num)
    num -= 0.5