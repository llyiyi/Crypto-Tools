def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = exgcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def solve(a, m):
    x, _, q = exgcd(a, m)
    if q != 1:
        raise Exception("No solution.")
    else:
        return (x + m) % m
