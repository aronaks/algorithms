# O(n)


def move_zeros(keys):
    i = 0
    j = len(keys) - 1
    while i < j:
        while keys[j] == 0 and j >= 0:
            j -= 1
        if i >= j:
            break
        if keys[i] == 0:
            tmp = keys[i]
            keys[i] = keys[j]
            keys[j] = tmp
            j -= 1
        i += 1
