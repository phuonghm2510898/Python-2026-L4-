def extract_even(l):
    even_list = []
    for x in l:
        if x % 2 == 0:
            even_list.append(x)
    return even_list

input = input("Enter list of integers: ")
l = [int(x) for x in input.split()]
res = extract_even(l)
print("List2: ", result)            