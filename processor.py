def select_from_menu():
    print("1. Add matrices")
    print("2. Multiply matrix by constant")
    print("3. Multiply matrices")
    print("0. Exit")
    return int(input("Your choice: "))


def input_matrix(matrix_message = "matrix"):
    n1, m1 = [int(x) if x.isdigit() else float(x) for x in input("Enter size of "
                                    + matrix_message + ": ").split()]
    print("Enter " + matrix_message + ":")
    A = [[int(x) if x.isdigit() else float(x) for x in input().split()] for _ in range(n1)]
    return A, n1, m1


def input_constant():
    return float(input("Enter constant: "))


def error_message():
    print("The operation cannot be performed.")


def print_result(matrix):
    print("The result is: ")
    for row in matrix:
        print(*row)


def add_matrices():
    A, n1, m1 = input_matrix("first matrix")
    B, n2, m2 = input_matrix("second matrix")
    if n1 == n2 and m1 == m2:
        C = [[a + b for a, b in zip(x, y)] for x, y in zip(A, B)]
        print_result(C)
    else:
        error_message()


def matrix_by_constant():
    A, n1, m1 = input_matrix("matrix")
    constant = input_constant()
    B = [[constant*x for x in row] for row in A]
    print_result(B)


def matrix_by_matrix():
    A, n1, m1 = input_matrix("first matrix")
    B, n2, m2 = input_matrix("second matrix")
    C = list()
    if m1 == n2:
        for i in range(n1):
            row = list()
            for j in range(m2):
                dotProduct = 0
                for k in range(m1):
                    dotProduct += A[i][k]*B[k][j]
                row.append(dotProduct)
            C.append(row)
        print_result(C)
    else:
        error_message()


def perform_operation(menu_option):
    if menu_option == 1:
        add_matrices()
    if menu_option == 2:
        matrix_by_constant()
    if menu_option == 3:
        matrix_by_matrix()
    print("\n")


def main():
    while True:
        option = select_from_menu()
        if option == 0:
            break
        perform_operation(option)


main()
