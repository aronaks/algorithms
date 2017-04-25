from algorithms.cracking1_1 import is_unique


def test_cracking1_1():
    keys = 'unique'
    res = is_unique(keys)
    assert res, 'String is not unique'
