from scipy.stats import ttest_rel
import numpy as np

before = np.array([
    # enter 10 before scores
    70, 72, 75, 77, 80, 82, 85, 87, 90, 92
])

after = np.array([
    # enter 10 after scores
    75, 78, 80, 82, 85, 87, 90, 92, 95, 98
])

difference = after - before

mean_difference = np.mean(difference)
sd_difference = np.std(difference, ddof=1)

t, p = ttest_rel(before, after)

print("Mean Difference =", mean_difference)
print("SD Difference =", sd_difference)
print("t-value =", t)
print("Degrees of Freedom =", len(before)-1)
print("p-value =", p)

if p < 0.05:
    print("Decision: Reject H0")
else:
    print("Decision: Fail to Reject H0")