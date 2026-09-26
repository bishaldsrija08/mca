class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __str__(self):
        return str(self.value)

a = Number(20)
b = Number(10)

print("a + b =", a + b)
print("a - b =", a - b)