def selection_sort(keys, keys_length):
    for j in range(keys_length):
        key = keys[j]
        min_key_index = j
        for i in range(j + 1, keys_length):
            if keys[min_key_index] > keys[i]:
                min_key_index = i
        keys[j] = keys[min_key_index]
        keys[min_key_index] = key
