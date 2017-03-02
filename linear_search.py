def find_v(keys, v):
    keys_length = len(keys)
    for i in range(keys_length):
        if keys[i] == v:
            return i
    return None
