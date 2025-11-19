import json

with open("land.json", encoding="utf-8") as fil:
    land_liste = json.load(fil)

def formater_innbyggere(innbyggere):
        if innbyggere < 1e3:
            return f"{innbyggere}"
        
        elif innbyggere < 1e6:
            innbyggere = innbyggere / 1e3
            return f"{innbyggere:.1f} tusener"
        
        elif innbyggere < 1e9:
            innbyggere = innbyggere / 1e6
            return f"{innbyggere:.1f} millioner"
        
        else:
            innbyggere = innbyggere / 1e9
            return f"{innbyggere:.1f} milliarder"

def skriv_ut_land(land):
    for key, verdi in land.items():
        if key == "innbyggere":
            print(f"{key.capitalize():10} : {formater_innbyggere(verdi)}")
        else:
            print(f"{key.capitalize():10} : {verdi}")
    print()

# India: 172
# Luxenbourg: 172 - 6
skriv_ut_land(land_liste[172-6])
skriv_ut_land(land_liste[172+1])
skriv_ut_land(land_liste[172])

print(f"Det er {len(land_liste)} antall land i filen")

innbyggere = 0
kontinenter = {}
for land in land_liste:
    innbyggere += land["innbyggere"]
    if land["kontinent"] in kontinenter:
        kontinenter[land["kontinent"]].append(land)
    else:
        kontinenter[land["kontinent"]] = [land]

print(f"Antall inbyggere i alle land: {formater_innbyggere(innbyggere)}")
print(f"Antall kontinenter: {len(kontinenter.keys())}")

def antall_land(kont):
    return len(kont[1])

sorterte_kontinenter = sorted(kontinenter.items(), reverse=True, key=antall_land)

print("\nKontinenter med flest land:")
for kontinent, land_liste in sorterte_kontinenter[:3]:
    print(f"{kontinent} har {len(land_liste)} antall land")

print()
for kontinent, land_liste in sorterte_kontinenter:
    innbyggere = 0
    for land in land_liste:
        innbyggere += land["innbyggere"]
    print(f"{kontinent} har {formater_innbyggere(innbyggere)} innbyggere")    
