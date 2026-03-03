from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasett_fodselstall.csv", encoding="utf-8",sep="\t")

# Første "fikset" jeg på kolonnene navnene
# Så la jeg til en index som var verdiene til
# År kolonnen og så slettet jeg År kolonnen. 
# Dette slik at datasettet da blir mer oversiktlig og enklere å håndtere
# Så droppet jeg rader som ikke inneholder noe data
# Til slutt gikk jeg igjennom dataene og endret kolonner med tekstverdier til tall

df.columns = ["År", "Fødte", "Innflyttinger", "Utflyttinger"]

df.index = df["År"]
df = df.drop(columns=["År"])
df = df.iloc[7:-1]
for kol in df:
    df[kol] = pd.to_numeric(df[kol])

print("a) uten de første årene og det siste.")
display(df)

df["netto folkevekst"] = df["Fødte"] + df["Innflyttinger"] - df["Utflyttinger"]

print("b) ")
display(df)

def hent_inn_data():
    """ Funksjon til å hente inn data fra brukeren"""
    
    while True:
        start = input("Tast inn start-år [1952-2023]: ")
        slutt = input("Tast inn slutt-år [1952-2023]: ")
        if not start.isnumeric() or not slutt.isnumeric():
            print("FEIL: Tast inn tallverdier")
            continue
        
        start, slutt = int(start), int(slutt)
        
        if not(1952 <= start <= 2023):
            print("FEIL: Start-år må ligge i intervallet [1952, 2023]")
            continue
        
        if not(1952 <= slutt <= 2023):
            print("FEIL: Slutt-år må ligge i intervallet [1952, 2023]")
            continue
        
        if slutt - start <= 0:
            print("FEIL: Slutt-år må være større enn start-år.")
            continue
    
        return start, slutt 

start, slutt = hent_inn_data()

df_plot = df["netto folkevekst"].iloc[start-1952:slutt-1952]
df_plot.plot.line()
plt.xlabel("År")
plt.ylabel("Nett befolkningsvekst")
plt.title(f"Befolkningsvekst mellom årene {start} - {slutt}")