import tkinter as tk

def find_greater():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if num1 > num2:
            result.config(text=f"Greater Number: {num1}")
        elif num2 > num1:
            result.config(text=f"Greater Number: {num2}")
        else:
            result.config(text="Both numbers are equal")
    except ValueError:
        result.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Greater Number")
root.geometry("350x250")

tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Find Greater", command=find_greater).pack(pady=15)

result = tk.Label(root, text="")
result.pack()

root.mainloop()