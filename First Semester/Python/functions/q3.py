# Create a function sum to find the sum of two numbers. Use this function to find the fibonacchi number.

def sum(a, b):
    return a + b

def fibo(n):
    if n<=0:
        return 0
    elif n==1 or n==0:
        return n
    else:
        return sum(fibo(n-1), fibo(n-2))
    
n = 10
for i in range (n):
    print(fibo(i), end= " ") # output: 0 1 1 2 3 5 8 13 21 34