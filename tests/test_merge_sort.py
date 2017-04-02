from algorithms.merge_sort import merge_sort, merge_sort_with_insertion_sort_for_small_values


def test_merge_sort():
    keys = [6, 7, 9, 12, 0, 1, 2]
    expected_res = sorted(keys)
    merge_sort(keys, 0, len(keys))
    assert keys == expected_res


def test_merge_sort_that_uses_insertion_sort():
    keys = [i for i in range(100, 0, -1)]
    expected_res = sorted(keys)
    merge_sort_with_insertion_sort_for_small_values(keys, 0, len(keys))
    assert keys == expected_res
