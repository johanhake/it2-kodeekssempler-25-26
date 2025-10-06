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
        print("\nALLE LAND I:", verdensdel)
        kost_verdier = []
        for d in filtrerte_data:
            if d[0] == verdensdel:
                kost_verdier.append(d[ind_kost])
                
        gjennomsnitt.append([verdensdel, int(sum(kost_verdier)/len(kost_verdier))])
        
    print(gjennomsnitt)
    
    # Henter ut alle kostverdier fra Asia
    lender_asia = []
    for d in filtrerte_data:
        if d[0] == "Asia":
            lender_asia.append(d)
    
    # Key funksjon for å sortere etter kost
    def kost_key(d):
        return d[ind_kost]
    
    # Sorterer fra størst til minst etter kost
    lender_asia_størst_minst = sorted(lender_asia, key=kost_key, reverse=True)
    
    # Skriver ut de tre lendene med størst kost
    for land in lender_asia_størst_minst[:3]:
        print(f"Land: {land[1]} kost: {land[ind_kost]}")