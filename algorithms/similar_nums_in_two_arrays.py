# O(n+m)


def count_similar_nums(keys1, keys2):
    """
    There are two arrays that are both sorted. I want you to design an algorithm
    to count the number of elements that these two arrays have in common.
    """
    i = j = 0
    common_elements_num = 0
    while i < len(keys1) and j < len(keys2):
        if keys1[i] > keys2[j]:
            j += 1
        elif keys1[i] < keys2[j]:
            i += 1
        else:
            common_elements_num += 1
            i += 1
            j += 1
    return common_elements_num
