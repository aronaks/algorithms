def merge(keys, leftmost_index, middle_index, rightmost_index):
    b = keys[leftmost_index:middle_index]
    c = keys[middle_index:rightmost_index]

    b.append(float("inf"))
    c.append(float("inf"))
    i = j = 0
    for k in range(leftmost_index, rightmost_index):
        if b[i] <= c[j]:
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

