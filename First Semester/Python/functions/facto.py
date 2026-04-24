# Write a function product to find the product of two numbers. Also write another function factorial to compute factorial of a number. Can you use the product function to compute factorial?


def product(a, b):
    return a * b

def factorial(n):
    if n == 0 or n ==  1:
        return 1
    else:
        return product(n, factorial(n-1))
    
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")