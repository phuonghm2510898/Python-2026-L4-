def remove_dollar_sign(s):
    return s.replace("$", "")

input = input("Text: ")
res = remove_dollar_sign(input)
print("Result = ", res)