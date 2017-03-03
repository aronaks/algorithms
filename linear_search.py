def find_v(keys, keys_length, v):
    for i in range(keys_length):
        if keys[i] == v:
            return i
    return None
