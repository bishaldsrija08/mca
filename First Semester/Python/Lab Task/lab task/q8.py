import tkinter as tk

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                output.config(text="Cannot divide by zero")
                return
            result = num1 / num2

        output.config(text=f"Result: {result}")

    except ValueError:
        output.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")

tk.Label(root, text="First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="+", width=5, command=lambda: calculate("+")).pack(pady=3)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).pack(pady=3)
tk.Button(root, text="*", width=5, command=lambda: calculate("*")).pack(pady=3)
tk.Button(root, text="/", width=5, command=lambda: calculate("/")).pack(pady=3)

output = tk.Label(root, text="")
output.pack(pady=10)

root.mainloop()