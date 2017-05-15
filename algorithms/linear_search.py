# O(n)


def find_v(keys, v):
    keys_length = len(keys)
    for i in range(keys_length):
        if keys[i] == v:
            return i
    return None


def recursive_linear_search(keys, i, v):
    keys_length = len(keys)
    if i >= keys_length:
        return "Not found"
    if keys[i] == v:
        return i
    else:
        return recursive_linear_search(keys, i + 1, v)
