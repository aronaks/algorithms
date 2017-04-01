from algorithms.binary_search import binary_search, binary_search_my_implementation


def test_binary_search():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_res = 9
    actual_res = binary_search(keys, len(keys), 10)
    assert actual_res == expected_res


def test_binary_search_my_implementation():
    keys = [1, 3, 4, 5, 8, 11, 13, 18]
    expected_res = len(keys) - 1
    actual_res = binary_search_my_implementation(keys, 0, len(keys), 18)
    assert actual_res == expected_res
