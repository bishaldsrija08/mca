A = {1, 2, 3}

R = {(1, 1), (2, 2), (3, 3),
     (1, 2), (1, 3), (2, 3)}

reflexive = all((a, a) in R for a in A)

antisymmetric = all(
    a == b or (b, a) not in R
    for (a, b) in R
)

transitive = all(
    (a, c) in R
    for (a, b) in R
    for (c, d) in R
    if b == c
)

if reflexive and antisymmetric and transitive:
    print("The relation is a Partial Order Relation.")
else:
    print("The relation is NOT a Partial Order Relation.")