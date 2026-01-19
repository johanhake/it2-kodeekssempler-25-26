import random
antall_terninger = 5

print('\nYatzy') # Fem like terninger, 
antall_kast = 5000
for n in range(antall_kast):
    res = []
    for i in range(antall_terninger):
        res.append(random.randint(1,6))
    if len(set(res))==1:
        print(res)

print('\nFire like') # Fire like terninger
antall_kast=100
for n in range(antall_kast):
    res = []
    for i in range(antall_terninger):
        res.append(random.randint(1,6))
    if len(set(res))==2:
        if res.count(res[0]) in (1,4):
            print(sorted(res))

print('\nHus') # Kombinasjon av tre like terninger og to like terninger av en annen verdi.
antall_kast=100
for n in range(antall_kast):
    res = []
    for i in range(antall_terninger):
        res.append(random.randint(1,6))
    if len(set(res))==2:
        if res.count(res[0]) in (2,3):
            print(sorted(res))

print('\nStor straight') # Kombinasjonen 2-3-4-5-6
antall_kast=100
for n in range(antall_kast):
    res = []
    for i in range(antall_terninger):
        res.append(random.randint(1,6))
    if len(set(res))==5 and 1 not in res:
        print(sorted(res))