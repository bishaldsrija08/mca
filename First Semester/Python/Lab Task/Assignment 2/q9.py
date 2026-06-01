# Write a recursive function to implement Tower of Hanoi problem.

def tower_hanoi(n, a,b,c):
    if n == 1:
        print("Move disk 1 from rod", a, "to rod", c)
        return
    tower_hanoi(n-1, a, c, b)
    print("Move disk", n, "from rod", a, "to rod", c)
    tower_hanoi(n-1, b, a, c)
    print("Move disk", n, "from rod", a, "to rod", c)

n = 2
tower_hanoi(n, 'A', 'B', 'C')