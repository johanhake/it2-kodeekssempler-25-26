import csv

# Funksjon som brukes som key for å sortere etter navn. 
# Den returnerer den første verdien, navn, i hver rad (data)
def navn_key(d):
    return d[0]

# Funksjon som brukes som key for å sortere etter alder
# Den returnerer den andre verdien, alder, i hver rad (data)
def alder_key(d):
    return d[1]

with open("navn.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    navn = []
    # Henter ut dataene og legger de i en ege liste
    for d in data:
        navn.append([d[0], int(d[1])])
    
    # Lager to lister, en sortert etter navn og en etter alder. 
    navn_alfabetisk = sorted(navn, key=navn_key)
    navn_alder = sorted(navn, key=alder_key)
    
    # Besvarer oppgaven
    print(f"Det er {len(navn)} navn i filen\n")
    print("Alfabetisk:")
    for d in navn_alfabetisk:
        print(d[0])
        
    # Eldst er siste elementet og yngst er første elementet i listen navn_alder
    eldst = navn_alder[-1]
    yngst = navn_alder[0]
    print(f"\nEldst: {eldst[0]}, Yngst: {yngst[0]}")