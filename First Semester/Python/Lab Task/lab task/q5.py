class Calculator:
    def add(self, *numbers):
        return sum(numbers)

c = Calculator()

print("Addition of two numbers:", c.add(10, 20))
print("Addition of three numbers:", c.add(10, 20, 30))
print("Addition of four numbers:", c.add(10, 20, 30, 40))