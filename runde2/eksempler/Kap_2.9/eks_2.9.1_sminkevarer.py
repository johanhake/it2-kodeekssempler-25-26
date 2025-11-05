import json

with open("sminkevarer.json") as fil:
    data = json.load(fil)

print(f"Det finnes {len(data)} antall varer totalt.")

# Bruk av forløkke til å hente ut alle varetypene
varetyper = []
for vare in data:
    varetyper.append(vare["product_type"])

varetyper = set(varetyper)

# Bruk av listcomprehensions
varetyper = set([vare["product_type"] for vare in data])

print(f"Antall ulike varetyper er: {len(varetyper)}")
print()

# "Fikser" pris egenskapene til hver vare. Foreløpig er det en str. Må endres til float for å kunne sammenlignes. Ser at noen har "0.0" som pris. Da blir de veeeeeldig billige...
for vare in data:
    # Finnes "price"?
    if vare["price"] is None:
        vare["price"] = 0.0
    else:
        vare["price"] = float(vare["price"])
        
# Lager ordbok med alle varetypene som nøkkler og liste med alle tilhørende varer som verdi
varer_dict = {}
for vare in data:
    if vare["product_type"] in varer_dict:
        # Legger til vare i listen til hver varetype
        varer_dict[vare["product_type"]].append(vare)
    else:
        # Varetypen finne IKKE fra før. Lager en ny liste med vare som første element
        varer_dict[vare["product_type"]] = [vare]

# Går igjennom alle varetypene og viser antallet varer per varetype
for key, liste in varer_dict.items():
    print(f"Det finnes {len(liste)} av varetypen: {key}")
    
# Funksjon som tar en vare-tuppel som argument og returnerer lengden av det andre elementet i tuppelen. Brukes for å sortere en liste med tupler med minst varer først. 
def lengde_varer(varer):
    return len(varer[1])

# Lager en liste med varetyper og varer
sortert_varer_list = sorted(varer_dict.items(), key=lengde_varer)

print()
print("Følgende varertyper har flest varer i seg")
# Uten forløkke først
print(f"{sortert_varer_list[-1][0]}: {len(sortert_varer_list[-1][1])}")
print(f"{sortert_varer_list[-2][0]}: {len(sortert_varer_list[-2][1])}")
print(f"{sortert_varer_list[-3][0]}: {len(sortert_varer_list[-3][1])}")

# Med forløkke bakfra -1 -> -4 steg: -1
print()
for vare_type, varer in sortert_varer_list[-1:-4:-1]:
    print(f"{vare_type}: {len(varer)}")
    
# Funksjon som tar en vare som argument og returnerer priset Brukes for å sortere en liste med varer etter pris
def pris_vare(vare):
    return vare["price"]

# Sortering etter pris. 
for vare_type in varer_dict:
    varer_dict[vare_type] = sorted(varer_dict[vare_type], key=pris_vare, reverse=True)
    
# Printer dyreste varen per varetype
print()
for vare_type, varer in varer_dict.items():
    print(f"Dyreste varen i {vare_type} er {varer[0]["price"]}")
