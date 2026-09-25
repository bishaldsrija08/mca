def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)

    if gcd != 1:
        return None

    return x % m


n = int(input("Enter number of congruences: "))

a = []
m = []

for i in range(n):
    a.append(int(input(f"Enter remainder a[{i+1}]: ")))
    m.append(int(input(f"Enter modulus m[{i+1}]: ")))

M = 1
for value in m:
    M *= value

x = 0

for i in range(n):
    Mi = M // m[i]
    yi = mod_inverse(Mi, m[i])
    x += a[i] * Mi * yi

x = x % M

print("Solution x =", x)
print("Modulo =", M)