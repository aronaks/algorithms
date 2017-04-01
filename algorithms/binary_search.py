def binary_search(keys, keys_length, v):
    leftmost_index = 1
    rightmost_index = keys_length - 1
    while leftmost_index <= rightmost_index:
        middle_index = int((leftmost_index + rightmost_index) / 2)
        if keys[middle_index] == v:
            return middle_index
        elif keys[middle_index] > v:
            rightmost_index -= 1
        else:
            leftmost_index += 1

    return "Not found"


def recursive_binary_search(keys, leftmost_index, rightmost_index, v):
    if rightmost_index < leftmost_index:
        return "Not found"
    middle_index = (leftmost_index + rightmost_index) / 2

    if keys[middle_index] == v:
        return middle_index
    elif keys[middle_index] > v:
        return recursive_binary_search(keys, leftmost_index, rightmost_index - 1, v)
    else:
        return recursive_binary_search(keys, leftmost_index + 1, rightmost_index, v)


def binary_search_my_implementation(keys, left, right, v):
    while left <= right:
        mp = int((left + right) / 2)
        if keys[mp] == v:
            return mp
        elif keys[mp] < v:
            left = mp
        else:
            right = mp
    return None
