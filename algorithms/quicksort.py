# O(n^2)


def partition(keys, p, r):
    q = p
    for u in range(p, r):
        if keys[u] <= keys[r]:
            keys[q], keys[u] = keys[u], keys[q]
            q += 1
    keys[q], keys[r] = keys[r], keys[q]
    return q


def quick_sort(keys, p, r):
    if p >= r:
        return
    q = partition(keys, p, r)
    quick_sort(keys, p, q - 1)
    quick_sort(keys, q + 1, r)
