from scipy.stats import f_oneway

A = [65,68,70,66,69]
B = [72,75,74,78,76]
C = [80,82,85,81,84]

F, p = f_oneway(A, B, C)

print("Mean A =", sum(A)/len(A))
print("Mean B =", sum(B)/len(B))
print("Mean C =", sum(C)/len(C))
print("F-statistic =", F)
print("p-value =", p)