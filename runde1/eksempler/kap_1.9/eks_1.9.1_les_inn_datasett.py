import csv

with open("2019.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    ind_kost = h.index("kost")
    print("indeks for kost:", ind_kost)
    print(h)
    for d in data:
        print(d)
