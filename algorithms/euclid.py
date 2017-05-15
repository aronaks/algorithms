# TODO: Fix the algorithm


def find_greatest_common_divisor(m, n):
    if m < n:
        m, n = n, m
    r = n % m
    if r == 0:
        return n
    return find_greatest_common_divisor(n, r)
