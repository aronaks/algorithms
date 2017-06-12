from algorithms.inversions import get_inversions_num


def test_inversions_num():
    keys = [i for i in range(600, 0, -1)]
    expected_res = int((pow(len(keys), 2) - len(keys)) / 2)
    inversions_num = get_inversions_num(keys, 0, len(keys))
    assert inversions_num == expected_res


def test_inversions_num2():
    keys = [1, 3, 5, 2, 4, 6]
    inversions_num = get_inversions_num(keys, 0, len(keys))
    expected_res = 3
    assert inversions_num == expected_res


def test_big_file_inversions_num():
    """
    Your task is to compute the number of inversions in the file given
    """

    with open('tests/test_data/IntegerArray.txt') as f:
        content_nums = [int(num) for num in f]
    inversions_num = get_inversions_num(content_nums, 0, len(content_nums))
    expected_res = 2407905288
    assert inversions_num == expected_res
