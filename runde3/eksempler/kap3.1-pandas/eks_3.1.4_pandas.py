import pandas as pd
from IPython.display import display

df = pd.read_csv("husholdningsregnskap.csv", sep=";", encoding="utf-8")

print("\n## head ##")
display(df.head())

print("\n## info ##")
df.info()

print("\n## kolonner og rader ##")
display(df.columns)
display(df.index)

print("\n## Enkelt kolonner ##")
display(df["dato"].head())
display(df[["dato", "beløp (kr)"]].head())

print("\n## Ny tabell hvor data oppfyller betingelse ##")
over_1500 = df["beløp (kr)"] > 1500
display(over_1500)
display(df[over_1500])

# Bare kolonnen dato
display(df[over_1500]["dato"])

# Fancy måte å hente ut februar dataene
februar = df["dato"].str.contains(f"\.02\.")
display(df[februar])

print("\n## Hente ut rader og kolonner med indekser ##")
display(df.iloc[[0,4,6]])
display(df.iloc[[0,4,6], [0,3]])


print("\n## Legge til og fjerne kolonner ##")
df["dobbelt"] = df["beløp (kr)"]*2
df["er mat"] = df["type"] == "mat"
display(df[["dobbelt", "er mat"]])

# Fjerne kolonner
df = df.drop(columns=["dobbelt", "er mat"])
display(df)

# Legge til en rad lengst ned (tenk append)
df.loc[len(df.index)] = ["30.03.2025", "mat", 1045, "oda"]
display(df.tail())

print("\n## Sortering ##")
display(df.sort_values("beløp (kr)", ascending=False))

print("\n## Sortering av ulike verdier##")
display(df.sort_values(["kommentar", "beløp (kr)"], ascending=[True, False]))

print("\n## Statistikk på enkelt grupper ##")
print("Gjennomsnitt gruppert på type")
display(df.groupby(df["type"]).mean(numeric_only=True))

print("Teller antall gruppert på type")
display(df.groupby(df["type"]).count())

print("Henter ut kommentarer sortert etter antall")
display(df.groupby(df["kommentar"]).count().sort_values("dato", ascending=False).index)

print("\n## Statistikk på enkelt grupper som er valgte ##")
print("januar")
display(df[df["dato"].str.contains("\.01\.")].groupby(df["type"]).sum(numeric_only=True))
print("februar")
display(df[df["dato"].str.contains("\.02\.")].groupby(df["type"]).sum(numeric_only=True))
print("mars")
display(df[df["dato"].str.contains("\.03\.")].groupby(df["type"]).sum(numeric_only=True))