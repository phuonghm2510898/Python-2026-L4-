n = int (input ("Number:"))
if n % 2 != 0:
    print (f("{n} is not a perfect number."))
else:
    sum_of_divisor = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisor += i


if sum_of_divisor == n and n>0:
    print (f"{n} est le nombre parfait.")
else:
    print (f"{n} n'est pas le nombre parfait.")

