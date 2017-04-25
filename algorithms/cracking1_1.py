# O(n * log n)


from algorithms.merge_sort import merge_sort


def is_unique(keys):
    """
    Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
    """
    merge_sort(list(keys), 0, len(keys))
    prev = keys[0]
    for i in range(1, len(keys)):
        if keys[i] == prev:
            return False
        prev = keys[i]
    return True
