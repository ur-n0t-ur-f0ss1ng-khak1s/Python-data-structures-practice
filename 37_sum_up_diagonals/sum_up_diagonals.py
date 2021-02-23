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
    """
    TL_diagonal = 0
    TR_diagonal = 0
    i = 0
    #j = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if j == i:
                TL_diagonal += matrix[i][j]
                #TR_diagonal += matrix[i][j]
            if j == len(matrix) - (i + 1):
                TR_diagonal += matrix[i][j]
            j += 1
        i += 1
    return TL_diagonal + TR_diagonal