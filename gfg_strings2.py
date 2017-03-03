def count_combinations(keys, keys_length):
    count = 1

    if keys_length == 1:
        return 1

    if keys[0] != keys[1]:
        count *= 2

    for i in range(1, keys_length-1):
        if (keys[i] == keys[i - 1]) and (keys[i] == keys[i + 1]):
            count *= 1

        elif (keys[i] == keys[i-1]) or (keys[i] == keys[i + 1]) or (keys[i - 1] == keys[i + 1]):
            count *= 2
        else:
            count *= 3

    if keys[-1] != keys[-2]:
        count *= 2
    return count
