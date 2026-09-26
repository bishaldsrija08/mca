import numpy as np

arr = np.ones((10, 10), dtype=int)

arr[1:-1, 1:-1] = 0

print("10x10 Array:")
print(arr)