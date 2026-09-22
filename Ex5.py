colors = ["Bleu", "Blanc", "Vert", "Rose", "Jaune"]

c = input("Coleur préférée: ")

if c in colors:
    index = colors.index(c)
    print(f"Your color is at index {index} in my list")
else:
    print(f"Sorry, I could not find your color")
