from algorithms.euclid import find_greatest_common_divisor


def test_find_greatest_common_divisor():
    res = find_greatest_common_divisor(244, 544)
    assert res == 1
