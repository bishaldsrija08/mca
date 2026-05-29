# Write a recursive function to compute the sum of numbers up to the input number.

def sum_up_to(n):
    if n <=0:
        return 0
    else:
        return n + sum_up_to(n-1)
    
n = int(input("Enter a number: "))
print(sum_up_to(n))