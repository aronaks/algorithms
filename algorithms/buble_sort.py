def bubble_sort(keys):
    keys_length = len(keys)
    for i in range(0, keys_length):
        for j in range(keys_length-1, i, -1):
            if keys[j] < keys[j-1]:
                keys[j], keys[j-1] = keys[j-1], keys[j]
