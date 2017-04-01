from algorithms.binary_search import binary_search


def test_binary_search():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_res = 9
    actual_res = binary_search(keys, len(keys), 10)
    assert actual_res == expected_res

