# 2-dimensional list of size 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original List:")
print(matrix)

print("\nFirst row:")
print(matrix[0][:])

print("\nFirst two rows:")
print(matrix[:2])

print("\nLast two rows:")
print(matrix[1:])

print("\nFirst two columns:")
print([row[:2] for row in matrix])

print("\nLast two columns:")
print([row[1:] for row in matrix])

print("\nMiddle element:")
print(matrix[1][1])