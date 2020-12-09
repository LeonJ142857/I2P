def multiply(a, b, row_a: int, column_b: int):
    res = 0
    row = a[row_a]
    column = [j[column_b] for j in b]
    for i, j in zip(row, column):
        res += i*j
    return res


def print_matrix(m, constant: float or int = 1):
    print("The result is:")
    for i in m:
        for j in i:
            print(j*constant, end=" ")
        print("")


def print_choice():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
    return int(input("Your choice: "))


choice = print_choice()
while choice != 0:
    if choice == 1 or choice == 3:
        r_A, c_A = map(int, input("Enter size of first matrix: ").split())  #
        print("Enter first matrix: ")  #
        A = [[eval(j) for j in input().split()] for i in range(r_A)]
        r_B, c_B = map(int, input("Enter size of second matrix: ").split())  #
        print("Enter second matrix: ")  #
        B = [[eval(j) for j in input().split()] for i in range(r_B)]
        result: list or str  #
        if choice == 1 and r_A == r_B and c_A == c_B:  #
            result = [[k+l for k, l in zip(i, j)]for i, j in zip(A, B)]  #
        elif choice == 3 and c_A == r_B:  #
            result = [[multiply(A, B, i, j) for j in range(c_B)] for i in range(r_A)]  #
        else:  #
            result = "The operation cannot be performed."  #
        if type(result) == str:  #
            print(result)  #
        else:  #
            print_matrix(result)  #
    elif choice == 2:
        r, c = map(int, input("Enter size of matrix: ").split())
        A = [[eval(j) for j in input().split()] for i in range(r)]
        cons: float = float(input("Enter constant: "))
        print_matrix(A, cons)
    print("")
    choice = print_choice()
