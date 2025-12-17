import csv
import numpy as np
import matplotlib.pyplot as plt

with open("medier-alder-utf8.csv", encoding="utf-8") as fil:
    data = csv.reader(fil, delimiter=";")
    internett = []
    aldersgrupper = []
    
    # Henter ut overskrifter og indekser til relevante data
    overskrifter = next(data)
    print(overskrifter)
    ind_2000 = overskrifter.index("2000")
    ind_medietype = overskrifter.index("medietype")
    årstall = np.array(overskrifter[ind_2000:], dtype=int)
    print(årstall)
    print("indeks for 2000", ind_2000)
    
    for rad in data:
        if rad[ind_medietype] == "Internett":
            print(rad[ind_2000:])
            internett_bruk = np.array(rad[ind_2000:], dtype=int)
            internett.append(internett_bruk)
            aldersgrupper.append(rad[2])
            plt.plot(årstall, internett_bruk, label=rad[2])
    print(internett)
    print(aldersgrupper)

    # Lager en numpy array for å kunne summere internettbruken for alle aldersgrupper
    internett_samlet = np.zeros(len(internett[0]), dtype=int)
    
    for internett_bruk in internett:
        internett_samlet += internett_bruk

    plt.plot(årstall, internett_samlet, label="Samlet")        
    plt.legend()
    plt.show()
        
print("Samlet internett bruk for alle aldre:", internett_samlet)
print("Årstall hvor det samlede Internettbruket er over 400: ", årstall[internett_samlet>400])