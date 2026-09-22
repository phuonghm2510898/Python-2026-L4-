def divisors(n):
    if n <= 0:
        return []
    
    div_list = []
    for i in range (1, n+1):
        if n % i == 0:
            div_list.append(i)
    return div_list

input = int(input("Enter an integer: "))
output = divisors(input)
print(f"All of the divisors of the number: {output}")
