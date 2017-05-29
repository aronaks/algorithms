from algorithms.move_zeros import move_zeros


def test_move_zeros():
    keys = [0, 12, 3, 0]
    move_zeros(keys)
    assert keys == [3, 12, 0, 0]


def test_move_zeros_all_zeros():
    keys = [0, 0, 0, 0]
    move_zeros(keys)
    assert keys == [0, 0, 0, 0]
