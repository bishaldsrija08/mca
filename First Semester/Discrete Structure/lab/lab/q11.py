A = [1, 2, 3]

R = {(1, 1), (1, 2), (2, 2), (3, 3)}

print("Relation Matrix:")

for i in A:
    for j in A:
        if (i, j) in R:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()