import numpy as np
from scipy.stats import ttest_ind

A = np.array([65,70,68,75,72,69,71,73])
B = np.array([72,75,70,78,80,74,77,76])

mean_A = np.mean(A)
mean_B = np.mean(B)

sd_A = np.std(A, ddof=1)
sd_B = np.std(B, ddof=1)

t, p = ttest_ind(A, B, equal_var=True)

print("Mean A =", mean_A)
print("SD A =", sd_A)
print("Mean B =", mean_B)
print("SD B =", sd_B)
print("t-value =", t)
print("p-value =", p)
print("Degrees of freedom =", len(A)+len(B)-2)