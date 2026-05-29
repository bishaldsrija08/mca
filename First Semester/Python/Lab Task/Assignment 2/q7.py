# Write functions to add, subtract, multiply and divide two numbers. Use these functions to calculate the value of
# x = a(b+c)(c-a)/(a+b-c) where a=5, b=2 and c=4.

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x/y

a = 5
b = 2
c = 4

calculation = divide(multiply(multiply(a, add(b,c)), subtract(c,a)), subtract(add(a,b), c))
print("The value of x is:", calculation)