from algorithms.fibonacci import fibonacci_numbers


def test_fibonacci():
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    res = map(fibonacci_numbers, range(13))
    assert fibonacci_sequence == list(res)
