import numpy as np
from scipy import stats

data = [10, 30, 50, 40, 20, 60, 70, 80, 90, 31, 25, 30]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True).mode[0]

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Q1 =", q1)
print("Q2 =", q2)
print("Q3 =", q3)