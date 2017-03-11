def sort_in_non_decreasing_mode(keys, keys_length):
    for j in range(1, keys_length):
        key = keys[j]
        i = j - 1
        while i >= 0 and keys[i] > key:
            keys[i + 1] = keys[i]
            i -= 1
        keys[i + 1] = key


def sort_in_non_increasing_mode(keys, keys_length):
    for j in range(1, keys_length):
        key = keys[j]
        i = j - 1
        while i >= 0 and keys[i] < key:
            keys[i + 1] = keys[i]
            i -= 1
        keys[i + 1] = key
