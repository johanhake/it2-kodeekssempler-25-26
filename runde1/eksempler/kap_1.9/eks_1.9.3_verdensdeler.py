import csv

with open("2019.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    ind_kost = h.index("kost")
    print("indeks for kost:", ind_kost)
    print(h)
    filtrerte_data = []
    verdensdeler = []
    for d in data:
        if d[ind_kost].isnumeric():
            d[ind_kost] = int(d[ind_kost])
            filtrerte_data.append(d)
        verdensdeler.append(d[0])
    
    # Bruker set til å fjerne alle duplikater
    verdensdeler = list(set(verdensdeler))
    verdensdeler = ["Afrika", "Europa", "Asia", "Amerika", "Australia/Oceania"]
    
    # Går igjennom alle verdensdeler
    gjennomsnitt = []
    for verdensdel in verdensdeler:
        print("\nALLE LENDER I:", verdensdel)
        kost_verdier = []
        for d in filtrerte_data:
            if d[0] == verdensdel:
                kost_verdier.append(d[ind_kost])
                
        gjennomsnitt.append([verdensdel, int(sum(kost_verdier)/len(kost_verdier))])
    
    print(gjennomsnitt)