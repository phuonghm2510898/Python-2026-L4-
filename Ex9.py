def factorial(n):
    if n < 0:
        return ("Error.")
    

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


input = int(input("Enter an integer: "))
output = factorial(input)
print(f"Factorial of the number: {output}")


