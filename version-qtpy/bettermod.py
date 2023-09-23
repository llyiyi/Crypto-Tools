def bettermod(a, c, m):
    less = 1
    for _ in range(1, c+1):
        less = (a*less) % m
    return less


def solve(a, c, m):
    return bettermod(a, c, m)
