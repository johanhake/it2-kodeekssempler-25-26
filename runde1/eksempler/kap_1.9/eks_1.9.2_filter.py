import csv

with open("2019.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    ind_kost = h.index("kost")
    print("indeks for kost:", ind_kost)
    print(h)
    filtrerte_data = []
    for d in data:
        if d[ind_kost].isnumeric():
            d[ind_kost] = int(d[ind_kost])
            filtrerte_data.append(d)
    
    asia = []
    
    for d in filtrerte_data:
        print(d)    

    print(filtrerte_data)
