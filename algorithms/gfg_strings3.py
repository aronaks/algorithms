def humming_distance(keys1, keys2, keys_length1, keys_length2):
    if keys_length1 != keys_length2:
        return "Lists do not have an equal size"

    count = 0

    for i in range(keys_length1):
        if keys1[i] != keys2[i]:
            count += 1
    return count
