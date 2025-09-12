maks = 21
print("  ", end="|")
for kolonne in range(1, maks):
    print(f"{kolonne:4}", end="")
print()
print("-"*maks*4)
for rad in range(1, maks):
    print(f"{rad:2} |", end="")
    for kolonne in range(1, maks):
        print(f'{rad*kolonne:3}', end=' ')
    print()