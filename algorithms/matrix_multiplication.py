from numpy import array

# O(n^3)


def multiply_matrices_brute_force(a, b):
    a_rows = a.shape[0]
    a_cols = a.shape[1]
    b_rows = b.shape[0]
    b_cols = b.shape[1]
    if a_cols != b_rows:
        return 0
    c = array([[None for _ in range(a_rows)] for _ in range(b_cols)])
    for i in range(a_cols):
        for j in range(a_cols):
            c[i][j] = 0
            for k in range(a_cols):
                c[i][j] += a[i][k] * b[k][j]
    return c


def multiply_square_matrices(a, b):
    a_rows = a.shape[0]
    a_cols = a.shape[1]
    b_rows = b.shape[0]
    b_cols = b.shape[1]
    if a_cols != b_rows:
        return 0
    c = array([[None for _ in range(a_rows)] for _ in range(b_cols)])
    if a_rows == 1 or b_rows == 1:
        c = a @ b
    else:
        a_rows_divided = int(a_rows / 2)
        a_cols_divided = int(a_cols / 2)
        b_rows_divided = int(b_rows / 2)
        b_cols_divided = int(b_cols / 2)

        c[0:a_rows_divided, 0:b_cols_divided] = multiply_square_matrices(
            a[0:a_rows_divided, 0:a_cols_divided], b[0:b_rows_divided, 0:b_cols_divided]) + multiply_square_matrices(
            a[0:a_rows_divided, a_cols_divided:a_cols], b[b_rows_divided:b_rows, 0:b_cols_divided])

        c[0:a_rows_divided, b_cols_divided:b_cols] = (multiply_square_matrices(
            a[0:a_rows_divided, 0:a_cols_divided], b[0:b_rows_divided, b_cols_divided:b_cols])
                                                      + multiply_square_matrices(
            a[0:a_rows_divided, a_cols_divided:a_cols], b[b_rows_divided:b_rows, b_cols_divided:b_cols]))

        c[a_rows_divided:a_rows, 0:b_cols_divided] = (multiply_square_matrices(
            a[a_rows_divided:a_rows, 0:a_cols_divided], b[0:b_rows_divided, 0:b_cols_divided])
                                                      + multiply_square_matrices(
            a[a_rows_divided:a_rows, a_cols_divided:a_cols], b[b_rows_divided:b_rows, 0:b_cols_divided]))

        c[a_rows_divided:a_rows, b_cols_divided:b_cols] = (multiply_square_matrices(
            a[a_rows_divided:a_rows, 0:a_cols_divided], b[0:b_rows_divided, b_cols_divided:b_cols]) +
                                                           multiply_square_matrices(
            a[a_rows_divided:a_rows, a_cols_divided:a_cols], b[b_rows_divided:b_rows, b_cols_divided:b_cols]))

    return c
