from scipy.stats import spearmanr

X = [25, 19, 28, 30, 18, 24]
Y = [58, 52, 65, 70, 51, 62]

rho, p = spearmanr(X, Y)

print("Spearman Correlation =", rho)
print("p-value =", p)