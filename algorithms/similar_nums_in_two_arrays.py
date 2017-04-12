# O(n+m)


def count_similar_nums(keys1, keys2):
    """
    There are two arrays that are both sorted. I want you to design an algorithm
    to count the number of elements that these two arrays have in common.
    """
    keys1_length = len(keys1)
    keys2_length = len(keys2)

    i = j = 0

    common_elements_num = 0
    while i < keys1_length and j < keys2_length:
        if keys1[i] > keys2[j]:
            j += 1
        elif keys1[i] < keys2[j]:
            i += 1
        else:
            common_elements_num += 1
            i += 1
            j += 1
    return common_elements_num
