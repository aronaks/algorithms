# O(n * log(n))


def find_max_crossing_subarray(keys, low, mid, high):
    i = left_index = mid
    left_sum = smallest_left = keys[i]
    while i > low:
        i -= 1
        left_sum += keys[i]
        if left_sum > smallest_left:
            smallest_left = left_sum
            left_index = i
    j = right_index = mid + 1
    right_sum = smallest_right = keys[j]
    while j < high:
        j += 1
        right_sum += keys[j]
        if right_sum > smallest_right:
            smallest_right = right_sum
            right_index = j
    total_sum = smallest_left + smallest_right
    return left_index, right_index, total_sum


def find_maximum_subarray(keys, low, high):
    if high == low:
        return low, high, keys[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(keys, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(keys, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(
            keys, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# O(n ^ 2)


def find_maximum_subarray_brute_force(keys):
    if len(keys) > 2:
        best_pair_sum = float('-inf')
        for i in range(len(keys)-1):
            j = i+1
            pair_sum = keys[i]
            for j in range(j, len(keys)):
                pair_sum += keys[j]
                if pair_sum >= best_pair_sum:
                    best_pair_sum = pair_sum
                    first_element_index = i
                    second_element_index = j
        return first_element_index, second_element_index, best_pair_sum
    raise Exception('Array should have more than 1 element')


