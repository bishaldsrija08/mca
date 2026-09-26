import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34, 67])

print("Original Array:")
print(arr)

print("\nAscending Order:")
print(np.sort(arr))

print("\nDescending Order:")
print(np.sort(arr)[::-1])

print("\nIndices of Sorted Array:")
print(np.argsort(arr))