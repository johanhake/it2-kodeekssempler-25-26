print("sort:")
venner = ["Ole", "Dole", "Doffen"]
print(venner)

# ['Doffen', 'Dole', 'Ole']
venner.sort()
print(venner)

print("sorted:")
venner = ["Ole           ", "Dole", "Doffen"]
print(sorted(venner))
# ['Doffen', 'Dole', 'Ole']
print(venner)

print("reversed:")
print(venner)
# ['Doffen', 'Dole', 'Ole']
venner.reverse()
print(venner)


def lengde(s):
    return len(s)


venner.sort(key=lengde)
print()
print(venner)

# Henter ut det andre alder (element med indeks 1)
def alder(l):
    return l[1]

lærere = [["Johan", 49], 
          ["Jarl", 57],
          ["Geir", 54], 
          ["Joar", 53]]

print(sorted(lærere, key=alder, reverse=True))