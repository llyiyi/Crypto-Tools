def x2tool(a, m):
    list = []
    for i in range(1, m):
        if (a+m) % m == (i*i) % m:
            list.append(i)
    return list


def Solve(a, m):
    list = x2tool(a, m)
    if len(list) == 0:
        return "No solution"
    else:
        return list
