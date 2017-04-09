from algorithms.gfg_arrays3 import find_repeated_elements


def test_find_repeated_elements():
    keys = [4, 2, 4, 5, 2, 3, 1]
    res = find_repeated_elements(keys)
    assert res == {2, 4}
