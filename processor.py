class Matrix:
    def __init__(self, size_message="Enter matrix size", value_message="matrix"):
        self.nrows, self.ncols = None, None
        self.values = None
        self.get_matrix_size(size_message)
        self.get_matrix_values(value_message)

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
    def error_message(self):
        print("The operation cannot be performed.")

    def add_matrix(self, matrix):
        if self.nrows == matrix.nrows and self.ncols == matrix.ncols:
            self.values = [[a + b for a, b in zip(x, y)] for x, y in zip(self.values, matrix.values)]
            self.print()
        else:
            self.error_message()

    def multiply_by_matrix(self, matrix):
        if self.ncols == matrix.nrows:
            self.values = [[sum([row[i] * matrix.values[i][j] for i in range(matrix.nrows)]) for j in range(matrix.ncols)] for row in self.values]
            self.print()
        else:
            self.error_message()

    @staticmethod
    def matrix_by_matrix(values1, nrows1, ncols1, values2, nrows2, ncols2):
        if ncols1 == nrows2:
            values = [[sum([row[i] * values2[i][j] for i in range(nrows2)]) for j in range(ncols2)] for row in values1]
            return values
        else:
            return Matrix.error_message()


    @staticmethod
    def multiply_by_constant(values, constant):
        return [[constant*x for x in row] for row in values]

    def diagonal_transpose(self, type_val=1):
        if type_val == 1:
            self.values = Matrix.transpose(self.values, self.nrows, self.ncols)
        else:
            self.values = [[self.values[j][i]  for j in range(self.nrows)[::-1]] for i in range(self.ncols)[::-1]]

    def line_transpose(self, type_val=3):
        if type_val == 3:
            self.values = [row[::-1] for row in self.values]
        else:
            self.values = [row for row in self.values[::-1]]

    @staticmethod
    def transpose(values, nrows, ncols):
        return [[values[j][i]  for j in range(nrows)] for i in range(ncols)]

    @staticmethod
    def determinant(values, nrows, ncols):
        if nrows == ncols == 1:
            return values[0][0]

        if nrows == ncols == 2:
            return values[0][0] * values[1][1] - values[0][1] * values[1][0]
        out_det = 0
        for i in range(ncols):
            minor = [[item for j, item in enumerate(row) if i != j] for row in values[1:]]
            out_det += values[0][i] * ((-1) ** (2 + i)) * Matrix.determinant(minor, nrows - 1, ncols - 1)
        return out_det

    @staticmethod
    def cofactors(values, nrows, ncols):
        cof_matrix = list()
        for i in range(nrows):
            local_row = list()
            for j in range(ncols):
                minor = [[item for l, item in enumerate(row) if l != j] for k, row in enumerate(values) if k != i]
                cof = ((-1) ** (2 + i + j)) * Matrix.determinant(minor, nrows - 1, ncols - 1)
                local_row.append(cof)
            cof_matrix.append(local_row)
        return cof_matrix

    @staticmethod
    def inverse(values, nrows, ncols):
        cof_matrix = Matrix.cofactors(values, nrows, ncols)
        det_value = Matrix.determinant(values, nrows, ncols)
        if det_value == 0:
            print("This matrix doesn't have an inverse.")
        else:
            inv_matrix = Matrix.multiply_by_constant(
                Matrix.transpose(cof_matrix, nrows, ncols), 1 / det_value)
        return inv_matrix


    def print_determinant(self):
        print("The result is:")
        print(self.determinant(self.values, self.nrows, self.ncols))


    def print_inverse(self):
        print("The result is:")
        inv_matrix = self.inverse(self.values, self.nrows, self.ncols)
        for row in inv_matrix:
            print(*row)
            # row_text = ""
            # for x in row:
            #     row_text += f"{round(x, 2) + 0: .2f} "
            # print(row_text.rstrip())


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


def input_constant():
    const = input("Enter constant: ")
    return int(const) if const.isdigit() else float(const)


def add_matrices():
    matrix1, matrix2 = input_matrices()
    matrix1.add_matrix(matrix2)


def multiply_matrices():
    matrix1, matrix2 = input_matrices()
    matrix1.multiply_by_matrix(matrix2)


def input_matrices():
    matrix1 = Matrix("Enter size of first matrix", "first matrix")
    matrix2 = Matrix("Enter size of second matrix", "second matrix")
    return matrix1, matrix2


def matrix_by_constant():
    matrix = Matrix("Enter size of matrix", "matrix")
    constant = input_constant()
    matrix.values = Matrix.multiply_by_constant(matrix.values, constant)
    matrix.print()


def transpose_matrix():
    transpose_type = select_transpose_type()
    if transpose_type in range(1, 5):
        matrix = Matrix("Enter matrix size", "matrix")
        if transpose_type <= 2:
            matrix.diagonal_transpose(transpose_type)
        else:
            matrix.line_transpose(transpose_type)
        matrix.print()


def calculate_determinant():
    matrix = Matrix("Enter matrix size", "matrix")
    matrix.print_determinant()


def inverse_matrix():
    matrix = Matrix("Enter matrix size", "matrix")
    matrix.print_inverse()


def perform_operation(menu_option):
    operations = [add_matrices, matrix_by_constant, multiply_matrices,
                    transpose_matrix, calculate_determinant, inverse_matrix]
    if menu_option in range(len(operations) + 1):
        operations[menu_option - 1]()
    print("\n")


def main():
    while True:
        option = select_from_menu()
        if option == 0:
            break
        perform_operation(option)

main()
