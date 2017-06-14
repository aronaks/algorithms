# O(n^3)


def multiply_matrices_brute_force(a, b):
    if len(a) != len(b[0]):
        return 0
    n = len(a)
    c = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c
