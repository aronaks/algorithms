from numpy import *
from numpy.testing import assert_array_equal

from algorithms.matrix_multiplication import (multiply_matrices_brute_force, multiply_square_matrices,
                                              multiply_matrices_strassen)


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


def test_multiply_matrices_strassen():
    a = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    b = array([[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]])
    res = multiply_matrices_strassen(a, b)
    assert_array_equal(res, array([[250, 260, 270, 280], [618, 644, 670, 696], [986, 1028, 1070, 1112],
                                   [1354, 1412, 1470, 1528]]))
