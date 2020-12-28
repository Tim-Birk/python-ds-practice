def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

        >>> m3 = [
        ...    [1, 2, 4, 3],
        ...    [4, 5, 4, 6],
        ...    [7, 8, 3, 9],
        ...    [1, 2, 7, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        34
    """
    drSum = 0
    dlSum = 0

    row_idx = 0
    reverse_row_idx = len(matrix[0]) -1 
    for row in matrix:
        drSum += matrix[row_idx][row_idx]
        dlSum += matrix[row_idx][reverse_row_idx]
        row_idx +=1
        reverse_row_idx -= 1
    return drSum + dlSum