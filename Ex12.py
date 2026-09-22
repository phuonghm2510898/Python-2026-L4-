def matrix_mn(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")


m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

matrix_mn(m, n)