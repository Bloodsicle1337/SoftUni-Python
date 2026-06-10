class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    size = len(matrix)

    for row in range(size):
        for col in range(row, size):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()


matrix = []

while True:
    row_data = input().split()

    if not row_data:
        break

    current_row = []

    for element in row_data:
        try:
            number = int(element)
            current_row.append(number)
        except ValueError:
            raise MatrixContentError("The matrix must consist of only integers")

    matrix.append(current_row)


rows_count = len(matrix)

for row in matrix:
    if len(row) != rows_count:
        raise MatrixSizeError("The size of the matrix is not a perfect square")


rotate_matrix(matrix)

for row in matrix:
    print(*row)