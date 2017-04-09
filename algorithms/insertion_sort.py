def sort_in_non_decreasing_mode(keys):
    keys_length = len(keys)
    for j in range(1, keys_length):
        key = keys[j]
        i = j - 1
        while i >= 0 and keys[i] > key:
            keys[i + 1] = keys[i]
            i -= 1
        keys[i + 1] = key


def sort_in_non_increasing_mode(keys):
    keys_length = len(keys)
    for j in range(1, keys_length):
        key = keys[j]
        i = j - 1
        while i >= 0 and keys[i] < key:
            keys[i + 1] = keys[i]
            i -= 1
        keys[i + 1] = key


def insertion_sort_rec(keys):
    if len(keys) == 1:
        return keys
    key = keys[-1]
    j = len(keys)-1
    res = insertion_sort_rec(keys[:j])
    res.append(key)
    i = j - 1
    while i >= 0 and key < res[i]:
        res[i+1] = res[i]
        i -= 1
    res[i+1] = key
    return res
