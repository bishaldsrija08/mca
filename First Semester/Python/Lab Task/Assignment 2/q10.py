# Perform slicing operations on a 2-dimensional list of size 3*3.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Slicing the rows
print("First row:", matrix[0])
print("Second row:", matrix[1])
print("Third row:", matrix[2])

# Slicing the columns
print("First column:", [row[0] for row in matrix])
print("Second column:", [row[1] for row in matrix])
print("Third column:", [row[2] for row in matrix])