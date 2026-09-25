A = {1, 2, 3}

R = {(1, 1), (2, 2), (3, 3),
     (1, 2), (2, 1),
     (2, 3), (3, 2),
     (1, 3), (3, 1)}

reflexive = all((a, a) in R for a in A)

symmetric = all(
    (b, a) in R
    for (a, b) in R
)

transitive = all(
    (a, c) in R
    for (a, b) in R
    for (c, d) in R
    if b == c
)

if reflexive and symmetric and transitive:
    print("The relation is an Equivalence Relation.")
else:
    print("The relation is NOT an Equivalence Relation.")