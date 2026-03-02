from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("friluftsaktiviteter.csv", encoding="utf-8",sep=";")

# Filtrerer ut fylkene fra de lange kolonne navnene
fylker = []
for navn in df.columns: 
    if navn != "friluftslivsaktivitet":
        fylker.append(navn.split()[5])
            
# Lager index til radene verdien til friluftslivsaktivitet
df.index = df["friluftslivsaktivitet"]
df = df.drop(columns=["friluftslivsaktivitet"])

# Bytter kolonne navn til litt mer lesbare
df.columns=fylker

# 8a) 
print("Sum alle aktiviteter")
display(df.sum(axis=1))
print("\nAlternativ sum alle aktiviteter")
for aktivitet in df.index:
    print(f"{aktivitet:56} | {df.loc[aktivitet].sum()}")

valg = ""
while valg == "" or valg not in fylker:
    valg = input("Skriv inn et fylke du skal vise aktiviteten til.")
    if valg not in fylker:
        print(f"{valg} er ikke et fylke. Velg en av: {', '.join(fylker)}")
    else:
        # Henter ut en ny serie med bare aktivitetene fra det fylket. Henter ut det som en DataFrame istedenfor en Series (bruker klammeparenteser inne i klammeparenteser)
        df_valg = df[[valg]]
        
        # Lager en ny kolonne med prosent
        df_valg["Prosent [%]"] = (df_valg[valg]/df_valg[valg].sum()*100).round(0)
        
        print()
        display(df_valg.sort_values(valg))
        
        # 8c) 
        # Bruker plot-modul som er innebygget i pandas!!
        df_diag = df[valg].sort_values(ascending=False)[:3]
        df_diag.plot.bar()
        plt.grid(axis="y")

        
        # Alternativ, bruker matplotlib slik vi har lært oss:
        aktiviteter = df_diag.index
        verdier = df_diag.values

        plt.figure()
        plt.barh(aktiviteter, verdier)
        plt.title(f"De tre aktivitetene i {valg} som har flest deltagere")
        plt.grid(axis="x")
        plt.show()
        #print(df_diag)