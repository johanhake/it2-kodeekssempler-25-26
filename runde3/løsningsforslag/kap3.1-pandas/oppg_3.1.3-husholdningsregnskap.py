import pandas as pd
from IPython.display import display

def vis(serie):
    # Viser dataene ved å bruke en serie som om det var en ordbok
    print("Type  | Verdi")
    print("-------------")
    for t, v in serie.items():
        print(f"{t:5} | {v:5}")

df = pd.read_csv("husholdningsregnskap.csv", sep=";", encoding="utf-8")

print("\n## Statistikk på enkelt grupper ##")
print("Sum gruppert på type")
vis(df.groupby(df["type"]).sum()["beløp (kr)"])

print("\n## Statistikk på enkelt grupper som er valgte ##")
print("\nJanuar")
vis(df[df["dato"].str.contains(".01.")].groupby(df["type"]).sum()["beløp (kr)"])

print("\nFebruar")
vis(df[df["dato"].str.contains(".02.")].groupby(df["type"]).sum()["beløp (kr)"])

print("\nMars")
vis(df[df["dato"].str.contains(".03.")].groupby(df["type"]).sum()["beløp (kr)"])

# Legge til en rad lengst ned (tenk append)
# C) oppgaven på prøven med å legge til noe på slutten
#df.loc[len(df.index)] = ["30.03.2025", "mat", 1045, "oda"]
#display(df.tail())
