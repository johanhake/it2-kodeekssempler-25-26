import json

with open("sminkevarer.json") as fil:
    data = json.load(fil)

print(f"Det finnes {len(data)} antall varer totalt.")

# Bruk av forløkker
varetyper = []
for vare in data:
    varetyper.append(vare["product_type"])

varetyper = set(varetyper)

# Bruk av listcomprehensions
varetyper = set([vare["product_type"] for vare in data])

print(f"Antall ulike varetyper er: {len(varetyper)}")

varer_dict = {}
for vare in data:
    if vare["product_type"] in varer_dict:
        # Legger til vare i listen til hver varetype
        varer_dict[vare["product_type"]].append(vare)
    else:
        varer_dict[vare["product_type"]] = [vare]

# Går igjennom alle varetypene
for key, liste in varer_dict.items():
    print(f"Det finnes {len(liste)} av varetypen: {key}")
    
# Funksjon som tar en vare-tuppel som argument og returnerer lengden av det andre elementet i tuppelen
def lengde_varer(varer):
    return len(varer[1])

# Lager en liste med varetyper og varer
sortert_varer_list = sorted(varer_dict.items(), key=lengde_varer)

print("Følgende varertyper har flest varer i seg")
# Uten forløkke først
print(f"{sortert_varer_list[-1][0]}: {len(sortert_varer_list[-1][1])}")
print(f"{sortert_varer_list[-2][0]}: {len(sortert_varer_list[-2][1])}")
print(f"{sortert_varer_list[-3][0]}: {len(sortert_varer_list[-3][1])}")

# Med forløkke bakfra -1 -> -4 steg: -1
for vare_type, varer in sortert_varer_list[-1:-4:-1]:
    print(f"{vare_type}: {len(varer)}")