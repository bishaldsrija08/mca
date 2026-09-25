# Example: 1 + 2 + ... + n = n(n+1)/2

def validate_induction(n):
    lhs = sum(range(1, n + 1))
    rhs = n * (n + 1) // 2

    return lhs == rhs


n = int(input("Enter value of n: "))

if validate_induction(n):
    print("The statement is verified for n =", n)
else:
    print("The statement is not verified.")