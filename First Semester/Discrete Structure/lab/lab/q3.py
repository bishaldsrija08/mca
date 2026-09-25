print("P\tQ\tP OR Q")
print("-" * 20)

for P in [True, False]:
    for Q in [True, False]:
        print(P, "\t", Q, "\t", P or Q)