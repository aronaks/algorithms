from algorithms.matrix_multiplication import multiply_matrices_brute_force


def test_multiply_matrices_brute_force():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    res = multiply_matrices_brute_force(a, b)
    assert res == [[19, 22], [43, 50]]
