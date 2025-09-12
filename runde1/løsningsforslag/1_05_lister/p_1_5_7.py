# Lag et program som ber brukeren skrive inn heltall
# som du legger inn i en liste. For hvert tall som legges inn,
# skal summen av alle tallene i listen skrives ut.
# Når brukeren trykker Enter uten å skrive inn et heltall,
# skal programmet skrive ut listen og avslutte.
# Før programmet avsluttes skal de største og laveste tallet
# fjernes fra listen samtidig som
# listen og gjennomsnittet av tallene skrives ut.
data  = []
total = 0
fortsett = True
while fortsett:
    tekst_inn = input('Skriv inn et heltall: ')
    if tekst_inn == '': fortsett = False
    if tekst_inn.isnumeric():
        data.append(int(tekst_inn))
        total = sum(data)
        print(f'Summen er nå {total}')
print(data)
tall_min = min(data)
while tall_min in data:
    data.remove(tall_min)
tall_max = max(data)
while tall_max in data:
    data.remove(tall_max)
from statistics import mean
gjsn = mean(data)
print(data)
print(f'Gjensomsittet uten min og maks er {gjsn:.2f}')

# Smidig IT-2 © TIP AS 2024