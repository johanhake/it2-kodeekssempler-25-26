import csv
import numpy as np

with open("medier-alder-utf8.csv", encoding="utf-8") as fil:
    data = csv.reader(fil, delimiter=";")
    internett = []
    aldersgrupper = []
    
    # Henter ut overskrifter og indekser til relevante data
    overskrifter = next(data)
    ind_2000 = overskrifter.index("2000")
    ind_medietype = overskrifter.index("medietype")
    årstall = np.array(??, dtype=int)
    
    for rad in data:
        ??

    # Lager en numpy array for å kunne summere internettbruken for alle aldersgrupper
    internett_samlet = np.zeros(len(internett[0]), dtype=int)
    
    for internett_bruk in internett:
        internett_samlet ??
        
print("Samlet internett bruk for alle aldre:", internett_samlet)
print("Årstall hvor det samlede Internettbruket er over 400: ", årstall[internett_samlet>400])