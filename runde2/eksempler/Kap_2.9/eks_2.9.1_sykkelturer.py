import json

with open("05.json") as fil:
    data = json.load(fil)

print(f"Det ble gjort {len(data)} antall sykkelturer totalt.")

# Bruker listkomprehensjon for å hente ut alle start-stasjonene, og så set for fjerne dubletter. 
ulike_start_lokalsjoner = set([tur["start_station_name"] for tur in data])
print(f"Det er {len(ulike_start_lokalsjoner)} ulike startlokasjoner.")

# Finner hvor mange ganger en  startlokasjon er blitt brukt
startlokasjoner = {}
for tur in data:
    if tur["start_station_name"] in startlokasjoner:
        startlokasjoner[tur["start_station_name"]] += 1
    else:
        startlokasjoner[tur["start_station_name"]] = 1
    
# Funksjon som henter ut den andre verdien i en tuppel som er antallet ganger en startlokasjon er blitt brukt
def antall(lokasjon):
    return lokasjon[1]
        
# Sorterer startlokasjonene etter antall mest brukte
startlokasjoner_sortert = sorted(startlokasjoner.items(), key=antall, reverse=True)

# printer ut de tre med flest antall turer fra:
print("\nFlest antall turer fra:")
for start_lokasjon, antall in startlokasjoner_sortert[:3]:
    print(f"Startlokasjon: {start_lokasjon} ble brukt {antall} ganger. ")
    
# printer ut de tre med færrest antall turer fra:
print("\nFærrest antall turer fra:")
for start_lokasjon, antall in startlokasjoner_sortert[-1:-4:-1]:
    print(f"Startlokasjon: {start_lokasjon} ble brukt {antall} ganger. ")