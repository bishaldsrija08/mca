a = 0
def square(x):
    global a
    a = a + 1
    return x * x

square(5)
print(a)