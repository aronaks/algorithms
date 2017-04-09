from algorithms.buble_sort import bubble_sort


def test_bubble_sort():
    keys = list(range(100, 0, -1))
    bubble_sort(keys)
    expected_result = sorted(keys)
    assert keys == expected_result
