from algorithms.insertion_sort import sort_in_non_decreasing_mode


def merge(keys, leftmost_index, middle_index, rightmost_index):
    b = keys[leftmost_index:middle_index]
    c = keys[middle_index:rightmost_index]
    i = j = 0
    for k in range(leftmost_index, rightmost_index):
        if i >= len(b):
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


def merge_sort(keys, leftmost_index, rightmost_index):
    if rightmost_index - leftmost_index <= 1:
        return keys
    middle_index = int(round((leftmost_index + rightmost_index) / 2.0))
    merge_sort(keys, leftmost_index, middle_index)
    merge_sort(keys, middle_index, rightmost_index)
    merge(keys, leftmost_index, middle_index, rightmost_index)


def merge_sort_with_insertion_sort_for_small_values(keys, leftmost_index, rightmost_index):
    if rightmost_index - leftmost_index <= 1:
        return keys
    elif rightmost_index - leftmost_index < 44:
        sort_in_non_decreasing_mode(keys)
    else:
        middle_index = int(round((leftmost_index + rightmost_index) / 2.0))
        merge_sort_with_insertion_sort_for_small_values(keys, leftmost_index, middle_index)
        merge_sort_with_insertion_sort_for_small_values(keys, middle_index, rightmost_index)
        merge(keys, leftmost_index, middle_index, rightmost_index)
