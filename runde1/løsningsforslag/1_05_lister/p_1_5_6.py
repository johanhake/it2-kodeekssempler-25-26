# Opprett en todimensjonal liste (8x8)
# som representerer et sjakkbrett,
# hvor hvert element er enten 'svart' eller 'hvit'
# Skriv ut listen rad for rad
# hvor rutene er justert kolonnevis.
brett = []
for i in range(8):
    rad = []
    for j in range(8):
        if (i+j) % 2 == 0:
            rad.append('hvit')
        else:
            rad.append('svart')
    brett.append(rad)

for rad in brett:
    for rute in rad:
        print(f'{rute:>6}', end='')
    print()

# Smidig IT-2 © TIP AS 2024