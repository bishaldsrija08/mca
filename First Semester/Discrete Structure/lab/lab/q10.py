A = {1, 2, 3}

R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}

reflexive = all((a, a) in R for a in A)

symmetric = all(
    (b, a) in R
    for (a, b) in R
)

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

print("Relation:", R)
print("Reflexive:", reflexive)
print("Symmetric:", symmetric)
print("Anti-symmetric:", antisymmetric)
print("Transitive:", transitive)