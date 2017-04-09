from algorithms.merge_sort import merge_sort


def find_repeated_elements(arr):
    """
    Find all numbers that repeat twice.
    """
    arr_length = len(arr)
    merge_sort(arr, 0, arr_length)
    repeated_elements = set()
    prev = arr[0]
    for i in range(1, arr_length):
        if arr[i] == prev:
            repeated_elements.add(arr[i])
        prev = arr[i]
    return repeated_elements
