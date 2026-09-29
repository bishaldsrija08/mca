import numpy as np
from scipy.stats import f

A = np.array([72,68,75,70,74,69,76,71])
B = np.array([65,80,70,75,68,82,73,78])

var_A = np.var(A, ddof=1)
var_B = np.var(B, ddof=1)

F = max(var_A, var_B) / min(var_A, var_B)

df1 = len(A) - 1
df2 = len(B) - 1

p = 2 * f.sf(F, df1, df2)

print("Variance A =", var_A)
print("Variance B =", var_B)
print("F-statistic =", F)
print("df1 =", df1)
print("df2 =", df2)
print("p-value =", p)