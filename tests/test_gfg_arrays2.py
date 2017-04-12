from algorithms.gfg_arrays2 import find_leaders


def test_find_leaders():
    arr = [16, 17, 4, 3, 5, 2]
    res = find_leaders(arr)
    assert [2, 5, 17] == res
