# Gitt listen tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a)	Bruk en for-løkke for å skrive ut hvert element
#       multiplisert med 10, på én linje.
# b)	Bruk listeutrulling (list comprehension)
#       til å lage  en ny liste som inneholder alle tallene
#       i tall økt med 5. Skriv ut den nye listen
tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for t in tall:
    print(f'{t*10:>4}', end='')
print()

ny_liste = [t+5 for t in tall]
print(ny_liste)

# Smidig IT-2 © TIP AS 2024