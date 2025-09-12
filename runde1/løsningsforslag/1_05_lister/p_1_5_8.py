# Bruk algoritmen Eratosthenes’ sil til å skrive ut alle primtallene under 100 i fem kolonner:
# •	Lag først en liste med tallene fra 2 til 100.
# •	Bruk det først tallet i tabellen (2) og fjern alle tallene i tabellen som er delelig med dette første tallet bortsett fra tallet selv.
# •	Bruk det neste tallet i tabellen (3) og fjern alle tallene i tabellen som er delelig med dette neste tallet bortsett fra tallet selv.
# •	Slik fortsetter du inntil du har testet tall mindre eller lik roten av 100, dvs 10.
# •	Skriv ut de gjenværende tallene (primtallene) i fem kolonner som vist under.
tabell = list(range(2, 101))
p = 0
while tabell[p] * tabell[p] <= 100:
    tall = tabell[p]
    for multiplum in range(tall * tall, 101, tall):
        if multiplum in tabell:
            tabell.remove(multiplum)
    p += 1    

print('\nPrimtall under 100:', end='')
for i in range(len(tabell)):
    if i % 5 == 0:
        print()
    print(f'{tabell[i]:5}', end='')

# Smidig IT-2 © TIP AS 2024