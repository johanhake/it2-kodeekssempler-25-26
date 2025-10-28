from planet import Planet
import csv

with open("planeter.csv", encoding="utf-8") as fil:
    planeter = []
    data = csv.reader(fil, delimiter=";")
    h = next(data)
    for d in data:
        p = Planet(d[0], float(d[1]), float(d[2]), int(d[3]))
        planeter.append(p)

for p in planeter:
    p.vis_info()
    print(f"Volumet til {p.navn} er {p.volum():.2e}")