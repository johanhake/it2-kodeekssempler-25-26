from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("energi_produksjon_forbruk_norge.csv", encoding="utf-8", sep=";")

# Setter år som index og dropper år kolonnen
df.index = df["År"]
df = df.drop(columns=["År"])

# Henter ut kolonnenavnene til produksjon og forbruk som lister
produksjon = df.columns[:4].to_list()
forbruk = df.columns[6:].to_list()

# Oppgave a)
# Summererer forbruk og produksjon
df["Total energiforbruk"] = df[forbruk].sum(axis=1)
df["Total energiproduksjon"] = df[produksjon].sum(axis=1)
display(df[df.index>2014][["Total energiforbruk", "Total energiproduksjon"]])

# Oppgave b)
df["Vannkraft prosentandel"] = (df["Vannkraftproduksjon"]/df["Total energiproduksjon"]*100).round(1)
display(df.sort_values("Vannkraftproduksjon", ascending=False).iloc[:5][["Vannkraftproduksjon", "Vannkraft prosentandel"]])

# Oppgave c)
valgt_år = int(input("Velg et år mellom 1960 og 2000"))
while not (1960 <= valgt_år <= 2000):
    valgt_år = int(input("Velg et år mellom 1960 og 2000"))

år = [i for i in range(valgt_år, 2025)]
df["Differanse"] = df["Import"] - df["Eksport"]
df["Eksport"] = -df["Eksport"]

df.loc[år][["Eksport", "Import", "Differanse"]].plot.line()
plt.ylabel("GWt energi")
plt.title(f"Eksport og Import av energi mellom {valgt_år} og 2025")





