def select_from_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("0. Exit")
    return int(input("Your choice: "))


def select_transpose_type():
    print("")
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    return int(input("Your choice: "))


def get_matrix_size(matrix_message = "Enter size of matrix"):
    n1, m1 = [int(x) if x.isdigit() else float(x) for x in input(matrix_message + ": ").split()]
    return n1, m1


def input_matrix(n1, m1, matrix_message = "matrix"):
    print("Enter " + matrix_message + ":")
    A = [[int(x) if x.isdigit() else float(x) for x in input().split()] for _ in range(n1)]
    return A


def input_constant():
    const = input("Enter constant: ")
    return int(const) if const.isdigit() else float(const)


def error_message():
    print("The operation cannot be performed.")


def print_result(matrix):
    print("The result is: ")
    for row in matrix:
        print(*row)


def add_matrices(A, n1, m1, B, n2, m2):
    if n1 == n2 and m1 == m2:
        C = [[a + b for a, b in zip(x, y)] for x, y in zip(A, B)]
        print_result(C)
    else:
        error_message()


def matrix_by_constant():
    n1, m1 = get_matrix_size("Enter size of matrix")
    A = input_matrix(n1, m1, "matrix")
    constant = input_constant()
    B = [[constant*x for x in row] for row in A]
    print_result(B)


def matrix_matrix(type_number=1):
    n1, m1 = get_matrix_size("Enter size of first matrix")
    A = input_matrix(n1, m1, "first matrix")
    n2, m2 = get_matrix_size("Enter size of second matrix")
    B = input_matrix(n2, m2, "second matrix")
    if type_number == 1:
        add_matrices(A, n1, m1, B, n2, m2)
    else:
        matrix_by_matrix(A, n1, m1, B, n2, m2)


def matrix_by_matrix(A, n1, m1, B, n2, m2):
    if m1 == n2:
        C = [[sum([row[i] * B[i][j] for i in range(n2)]) for j in range(m2)] for row in A]
        print_result(C)
    else:
        error_message()


def transpose_matrix():
    transpose_type = select_transpose_type()
    if transpose_type in range(1, 5):
        n1, m1 = get_matrix_size("Enter matrix size")
        matrix = input_matrix(n1, m1, "matrix")
        if transpose_type <= 2:
            diagonal_transpose(matrix, n1, m1, transpose_type)
        else:
            line_transpose(matrix, transpose_type)


def diagonal_transpose(matrix, nrows, ncols, type_number=1):
    if type_number == 1:
        new_matrix = [[matrix[j][i]  for j in range(nrows)]
                for i in range(ncols)]
    else:
        new_matrix = [[matrix[j][i]  for j in range(nrows)[::-1]]
                for i in range(ncols)[::-1]]
    print_result(new_matrix)


def line_transpose(matrix, type_number=3):
    if type_number == 3:
        new_matrix = [row[::-1] for row in matrix]
    else:
        new_matrix = [row for row in matrix[::-1]]
    print_result(new_matrix)


def perform_operation(menu_option):
    if menu_option in [1, 3]:
        matrix_matrix(menu_option)
    elif menu_option == 2:
        matrix_by_constant()
    elif menu_option == 4:
        transpose_matrix()
    print("\n")


def main():
    while True:
        option = select_from_menu()
        if option == 0:
            break
        perform_operation(option)


main()
