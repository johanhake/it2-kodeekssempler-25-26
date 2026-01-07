
import csv 
import matplotlib.pyplot as plt
import numpy as np
with open("husholdningsregnskap.csv", encoding="utf-8") as fil:
    data = csv.reader(fil, delimiter=";")
    overskrifter = next(data)
    
    # Lager en datastruktur innkjøp, ordbok med ordbøker
    # For å hente ut data fra csv filen
    måneder = ["Jan", "Feb", "Mars", "April", "Mai", "osv"]
    måneder_med_utgifter = []
    innkjøp = {}
    for måned in måneder + ["total"]:
        innkjøp[måned] = {
            "strøm":0,
            "mat":0,
        }
    # Går igjennom rad for rad i filen og henter ut dataene
    for rad in data:
        mån_nr = int(rad[0][3:5]) # int(rad[0].split(".")[1])->"03.01.26"
        måned = måneder[mån_nr-1]
        måneder_med_utgifter.append(måned)
        type = rad[1]
        beløp = int(rad[2])
        innkjøp[måned][type] += beløp
        innkjøp["total"][type] += beløp

# Finner de måneder som er registrerte med utgifter
måneder_med_utgifter = set(måneder_med_utgifter)

# Hviser hvor mye totale utgifter husholdningen har
for hva in ["strøm", "mat"]:
    print(f"Total beløp brukt på {hva}: {innkjøp['total'][hva]} kr")

# Hviser hvor mye totale utgifter husholdningen har og henter ut verdier som kan vises i en graf
# Bruker nøklene til innkjøp-ordboken
for måned in måneder:
    if måned in måneder_med_utgifter:
        print("")
        for hva in ["strøm", "mat"]:
            print(f"Beløp brukt på {hva} i {måned}: {innkjøp[måned][hva]} kr")

# Funksjon som legger til en utgift
def leggtil(dato, type, beløp, kommentar):
    "Legger til utgift til regnskapet"
    with open("husholdningsregnskap.csv", "a", encoding="utf-8") as fil:
        fil.write(f"{dato};{type};{beløp};{kommentar}\n")

#leggtil("29.03.2025", "mat", 405, "oda")
print("\nSiste raden i filen husholdningsregnskap:")
with open("husholdningsregnskap.csv", encoding="utf-8") as fil:
    print(fil.readlines()[-1])
    
