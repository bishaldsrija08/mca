# Write a function that computes factorial of a number if the input number is more than 5.

def factorial(n):
    if n > 5:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(6))
print(factorial(5))