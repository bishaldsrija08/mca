print("P\tQ\tP <-> Q")
print("-" * 20)

for P in [True, False]:
    for Q in [True, False]:
        result = P == Q
        print(P, "\t", Q, "\t", result)