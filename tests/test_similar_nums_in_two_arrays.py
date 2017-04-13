from algorithms.similar_nums_in_two_arrays import count_similar_nums


def test_find_similar_nums_positive_case():
    keys1 = [3, 5, 10, 15, 20, 25, 30, 35]
    keys2 = [2, 5, 7, 10, 25, 27]
    expected_num = 3
    actual_num = count_similar_nums(keys1, keys2)
    assert actual_num == expected_num


def test_find_similar_nums_negative_case():
    keys1 = range(19)
    keys2 = range(21, 100)
    expected_num = 0
    actual_num = count_similar_nums(keys1, keys2)
    assert actual_num == expected_num
