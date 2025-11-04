import json

with open("p_2_8_3.json") as fil:
    data = json.load(fil)
    
    for merke, modeller in data.items():
        print(merke)
        for modell in modeller:
            print(f"  modell: {modell['modell']}")
            print(f"  farge : {modell['farge']}")
            print()