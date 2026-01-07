import json

with open("land.json", encoding="utf-8") as fil:
    land_liste = json.load(fil)
    
teller = {"små":0, "middels":0, "store":0}
for land in land_liste:
    if land["innbyggere"] < 1e6:
        teller["små"] += 1
    elif land["innbyggere"] < 1e8:
        teller["middels"] += 1
    else:
        teller["store"] += 1

print("Små, middels og store land")
for type, antall in teller.items():
    print(f"Det er {antall:3} land som er {type}.")

print("\nDe 10 landene med flest innbyggere")

land_sortert = sorted(land_liste, key=lambda land:land["innbyggere"], reverse=True)
land_sortert_10_største = land_sortert[:10]

for land in land_sortert_10_største:
    print(f"{land['land']} har {land['innbyggere']/1e6:.1f} mill. innbyggere")
    
print("\nDe 10 største landene sortert etter befolkningstetthet")

for land in land_sortert_10_største:
    if land["areal"]>0:
        land["tetthet"] = land["innbyggere"]/land["areal"]
    else:
        land["tetthet"] = land["innbyggere"]

land_sortert_10_største_tetthet = sorted(land_sortert_10_største, key=lambda land:land["tetthet"], reverse=True)

for land in land_sortert_10_største_tetthet:
    print(f"{land['land']} har {land['tetthet']:.1f} innbyggere per kvm")
