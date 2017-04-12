def count(keys, leftmost_index, middle_index, rightmost_index):
    b = keys[leftmost_index:middle_index]
    c = keys[middle_index:rightmost_index]
    i = j = inversions_num = 0
    for k in range(leftmost_index, rightmost_index):
        if i >= middle_index:
            keys[k] = c[j]
            j += 1
        elif j >= len(c):
            keys[k] = b[i]
            i += 1
        elif b[i] <= c[j]:
            keys[k] = b[i]
            i += 1
        else:
            keys[k] = c[j]
            j += 1
            inversions_num += middle_index - leftmost_index
    return inversions_num


def get_inversions_num(keys, leftmost_index, rightmost_index):
    """
    Give an algorithm that determines the number of inversions in any 
    permutation on n elements in n log n worst-case time. (Hint: Modify merge 
    sort.)
    """
    if rightmost_index - leftmost_index <= 1:
        return 0
    inversion_counter = 0
    middle_index = int(round((leftmost_index + rightmost_index) / 2.0))
    inversion_counter += get_inversions_num(keys, leftmost_index, middle_index)
    inversion_counter += get_inversions_num(keys, middle_index, rightmost_index)
    inversion_counter += count(keys, leftmost_index, middle_index,
                               rightmost_index)
    return inversion_counter
