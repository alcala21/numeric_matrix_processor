class ErrorMessage:
    def __init__(self, message_type=1):
        if message_type == 1:
            self.message = "The operation cannot be performed."
        elif message_type == 2:
            self.message = "This matrix doesn't have an inverse."

    def print(self):
        return print(self.message)


class Matrix:
    def __init__(self, values=None, nrows=0, ncols=0, size_message="Enter matrix size", value_message="matrix"):
        if values is None:
            values = []
        self.values = values
        self.nrows = nrows
        self.ncols = ncols
        if not values:
            self.get_matrix_size(size_message)
            self.get_matrix_values(value_message)
        elif nrows == ncols == 0:
            self.nrows = len(values)
            self.ncols = len(values[0])

    def get_matrix_size(self, matrix_message="Enter size of matrix"):
        self.nrows, self.ncols = [int(x) if x.isdigit() else float(x) for x in input(matrix_message + ": ").split()]

    def get_matrix_values(self, matrix_message="matrix"):
        print("Enter " + matrix_message + ":")
        self.values = [[int(x) if x.isdigit() else float(x) for x in input().split()] for _ in range(self.nrows)]

    def print(self):
        print("The result is: ")
        for row in self.values:
            print(*row)

    @staticmethod
    def sum_matrices(matrix1, matrix2):
        if matrix1.nrows == matrix2.nrows and matrix1.ncols == matrix2.ncols:
            values = [[a + b for a, b in zip(x, y)] for x, y in zip(matrix1.values, matrix2.values)]
            return Matrix(values)
        else:
            return ErrorMessage()

    @staticmethod
    def matrix_by_matrix(matrix1, matrix2):
        if matrix1.ncols == matrix2.nrows:
            values = [[sum([row[i] * matrix2.values[i][j] for i in range(matrix2.nrows)]) for j in range(matrix2.ncols)]
                      for row in matrix1.values]
            return Matrix(values)
        else:
            return ErrorMessage()

    @staticmethod
    def matrix_by_constant(matrix, constant):
        return Matrix([[constant * x for x in row] for row in matrix.values])

    @staticmethod
    def diagonal_transpose(matrix, type_val=1):
        if type_val == 1:
            return Matrix([[matrix.values[j][i] for j in range(matrix.nrows)] for i in range(matrix.ncols)])
        else:
            return Matrix([[matrix.values[j][i] for j in range(matrix.nrows)[::-1]] for i in range(matrix.ncols)[::-1]])

    @staticmethod
    def line_transpose(matrix, type_val=3):
        if type_val == 3:
            return Matrix([row[::-1] for row in matrix.values])
        else:
            return Matrix([row for row in matrix.values[::-1]])

    @staticmethod
    def det(matrix):
        if matrix.nrows == matrix.ncols == 1:
            return matrix.values[0][0]
        if matrix.nrows == matrix.ncols == 2:
            return matrix.values[0][0] * matrix.values[1][1] - matrix.values[0][1] * matrix.values[1][0]
        out_det = sum([x * ((-1) ** (2 + i)) * Matrix.det(Matrix.minor(matrix, 0, i)) for i, x in enumerate(matrix.values[0])])
        return out_det

    @staticmethod
    def minor(matrix, row_index, col_index):
        return Matrix([row[:col_index] + row[col_index + 1:] for row in (matrix.values[:row_index] + matrix.values[row_index + 1:])])

    @staticmethod
    def adjoint(matrix):
        cof_values = list()
        for i in range(matrix.nrows):
            local_row = list()
            for j in range(matrix.ncols):
                minor = Matrix.minor(matrix, i, j)
                cof = ((-1) ** (2 + i + j)) * Matrix.det(minor)
                local_row.append(cof)
            cof_values.append(local_row)
        return Matrix.diagonal_transpose(Matrix(cof_values), 1)

    @staticmethod
    def inverse(matrix):
        det_value = Matrix.det(matrix)
        if det_value == 0:
            return ErrorMessage(2)
        return Matrix.matrix_by_constant(Matrix.adjoint(matrix), 1 / det_value)


def input_constant():
    const = input("Enter constant: ")
    return int(const) if const.isdigit() else float(const)


def add_matrices():
    Matrix.sum_matrices(*input_matrices()).print()


def multiply_matrices():
    Matrix.matrix_by_matrix(*input_matrices()).print()


def input_matrices():
    matrix1 = Matrix(size_message="Enter size of first matrix", value_message="first matrix")
    matrix2 = Matrix(size_message="Enter size of second matrix", value_message="second matrix")
    return matrix1, matrix2


def input_matrix(message_type=0):
    if message_type == 0:
        return Matrix(size_message="Enter size of matrix",
                      value_message="matrix")
    return Matrix(size_message="Enter matrix size",
                  value_message="matrix")


def matrix_by_constant():
    Matrix.matrix_by_constant(input_matrix(), input_constant()).print()


def transpose_matrix():
    transpose_type = select_transpose_type()
    if transpose_type in range(1, 5):
        matrix = input_matrix(1)
        if transpose_type <= 2:
            Matrix.diagonal_transpose(matrix, transpose_type).print()
        else:
            Matrix.line_transpose(matrix, transpose_type).print()


def calculate_determinant():
    matrix = input_matrix(1)
    print("The result is:")
    print(Matrix.det(matrix))


def inverse_matrix():
    Matrix.inverse(input_matrix(1)).print()


def perform_operation(menu_option):
    operations = [add_matrices, matrix_by_constant, multiply_matrices,
                  transpose_matrix, calculate_determinant, inverse_matrix]
    if menu_option in range(len(operations) + 1):
        operations[menu_option - 1]()
    print("\n")


def select_from_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    return int(input("Your choice: "))


def select_transpose_type():
    print("")
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    return int(input("Your choice: "))


def main():
    while True:
        option = select_from_menu()
        if option == 0:
            break
        perform_operation(option)


main()
