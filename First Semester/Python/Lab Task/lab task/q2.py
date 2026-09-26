pairs = [(2, 3), (1, 4), (4, 2), (5, 6), (6, 2)]

def add(a, b):
    return a + b

sums = [add(a, b) for a, b in pairs]

print("Ordered Pairs:")
print(pairs)

print("Sum of each ordered pair:")
print(sums)