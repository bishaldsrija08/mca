print("P\tQ\tP AND Q")
print("-" * 20)

for P in [True, False]:
    for Q in [True, False]:
        print(P, "\t", Q, "\t", P and Q)