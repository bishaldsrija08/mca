# Example: P OR NOT P

is_tautology = True

for P in [True, False]:
    result = P or not P
    print("P =", P, "Result =", result)

    if not result:
        is_tautology = False

if is_tautology:
    print("The proposition is a tautology.")
else:
    print("The proposition is not a tautology.")