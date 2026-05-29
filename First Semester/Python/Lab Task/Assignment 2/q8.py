# Write a function to find the power of a number using lambda function.

power = lambda x, y: x ** y

number = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = power(number, exponent)
print(f"{number} raised to the power of {exponent} is: {result}")