from algorithms.insertion_sort import sort_in_non_decreasing_mode


def test_insertion_sort():
    keys = [157, 406, 415, 318, 472, 46, 252, 187]
    sort_in_non_decreasing_mode(keys)
    assert sorted(keys) == keys
