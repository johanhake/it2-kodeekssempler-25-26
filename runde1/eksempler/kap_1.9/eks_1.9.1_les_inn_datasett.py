import csv

with open("2019.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    print(h)
    for d in data:
        print(d)
