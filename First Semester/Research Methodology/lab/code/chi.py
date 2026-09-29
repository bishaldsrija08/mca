import numpy as np
from scipy.stats import chi2_contingency

data = np.array([
    [45, 25],
    [35, 15]
])

chi2, p, df, expected = chi2_contingency(data, correction=False)

print("Chi-Square =", chi2)
print("Degrees of Freedom =", df)
print("p-value =", p)
print("Expected Frequencies:")
print(expected)