from numpy import *
from numpy.testing import assert_array_equal

from algorithms.matrix_multiplication import multiply_matrices_brute_force, multiply_square_matrices


def test_multiply_matrices_brute_force():
    a = array([[1, 2], [3, 4]])
    b = array([[5, 6], [7, 8]])
    res = multiply_matrices_brute_force(a, b)
    assert_array_equal(res, array([[19, 22], [43, 50]]))


def test_multiply_matrices_recursively_case1():
    a = array([[1, 2], [3, 4]])
    b = array([[5, 6], [7, 8]])
    res = multiply_square_matrices(a, b)
    assert_array_equal(res, array([[19, 22], [43, 50]]))


def test_multiply_matrices_recursively_case2():
    a = array([[1, 2, 3], [4, 5, 6]])
    b = array([[7, 8], [9, 10], [11, 12]])
    res = multiply_square_matrices(a, b)
    assert_array_equal(res, array([[58, 64], [139, 154]]))
