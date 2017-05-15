from algorithms.maximum_subarray import (find_maximum_subarray,
                                         find_maximum_subarray_brute_force)


def test_maximum_subarray_book_case():
    keys = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left, right, res = find_maximum_subarray(keys, 0, len(keys)-1)
    expected_left, expected_right, expected_res = 7, 10, 43
    assert (left, right, res) == (expected_left, expected_right, expected_res)


def test_maximum_subarray_simple_case():
    keys = range(-1, 3)
    left, right, res = find_maximum_subarray(keys, 0, len(keys)-1)
    expected_left, expected_right, expected_res = (2, 3, 3)  # the correct result might be (1, 3, 3) also
    assert (left, right, res) == (expected_left, expected_right, expected_res)


def test_brute_force_solution():
    keys = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    first, second, res = find_maximum_subarray_brute_force(keys)
    expected_first, expected_second, expected_res = 7, 10, 43
    assert (first, second, res) == (expected_first, expected_second,
                                    expected_res)


