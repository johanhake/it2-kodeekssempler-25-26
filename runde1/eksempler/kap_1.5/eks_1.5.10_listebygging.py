#  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
kvadrater = [x**2 for x in range(1, 11)]
print("Kvadrater:\n", kvadrater)

# [2, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 32, 42, 52, 62, 72, 82, 92]
tall = [x for x in range(1, 101) if "2" in str(x)]
print("\nTall med siffer 2:", end="")
print(tall)

tabell = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nTabell:")
for rad in tabell:
    print(rad)
flat_liste = [tall for rad in tabell for tall in rad]
print("\nFlat liste:\n", flat_liste)