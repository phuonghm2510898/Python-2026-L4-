import math
n = int(input("Enter a number: "))

prime = True

if n <= 1:
    prime = False
else:
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break

if prime:
    print (f"{n} is a prime number.")
else:
    print (f"{n} is not a prime number.")