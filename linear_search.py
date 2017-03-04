def find_v(keys, keys_length, v):
    for i in range(keys_length):
        if keys[i] == v:
            return i
    return None


def recursive_linear_search(keys, keys_length, i, v):
    if i >= keys_length:
        return "Not found"
    if keys[i] == v:
        return i
    else:
        return recursive_linear_search(keys, keys_length, i + 1, v)
