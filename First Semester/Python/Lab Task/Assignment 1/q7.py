"""
Use a conditional (ternary) operator for this exercise:
If the variable age is a value below 18, the value of the variable voteable should be "Too young", otherwise the value of voteable should be "Old enough".
"""
age = int(input("Enter your age: "))

votable = "Too young" if age < 18 else "Old enough"
print(votable)