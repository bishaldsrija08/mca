# Write a function that takes a number as input and checks whether the input number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))