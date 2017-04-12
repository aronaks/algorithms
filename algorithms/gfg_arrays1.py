from algorithms.merge_sort import merge_sort


def is_there_sum_of_two_elements(keys, v):
    """
    Write a function that, given an array of n numbers and another number x, 
    determines whether or not there exist two elements in the array whose sum is 
    exactly x. 
    """
    keys_length = len(keys)
    leftmost_index = 0
    rightmost_index = keys_length - 1
    merge_sort(keys, leftmost_index, rightmost_index)
    while leftmost_index < rightmost_index:
        if keys[leftmost_index] + keys[rightmost_index] == v:
            return True
        elif keys[leftmost_index] + keys[rightmost_index] < v:
            leftmost_index += 1
        else:
            rightmost_index -= 1
    return False
