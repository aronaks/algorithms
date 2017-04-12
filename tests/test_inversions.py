from algorithms.inversions import get_inversions_num


def test_merge_sort_that_uses_insertion_sort():
    keys = [i for i in range(6, 0, -1)]
    expected_res = int((pow(len(keys), 2) - len(keys)) / 2)
    inversions_num = get_inversions_num(keys, 0, len(keys))
    assert inversions_num == expected_res
