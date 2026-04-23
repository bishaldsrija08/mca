def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))


f= square
f(4)
print(f(4))


def fxy(f, x, y):
    return f(x) + f(y)

print(fxy(square, 3, 4))