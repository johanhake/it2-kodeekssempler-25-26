from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("05994_20240126-145813-csv.csv", encoding="utf-8",sep=";")

# Finner rader med aktivitetene og kategoriene
df.columns = ["Aktivitet", "Kjønn", "Tidsbruk"]
ind_aktiviteter = df["Aktivitet"].str.contains("¬") # Boolsk array
ind_kategorier = ind_aktiviteter==False  # Bytter verdiene
ind_kategorier[:3] = False # Fjerne "I alt" fra kategoriene

df_aktiviteter = df[ind_aktiviteter]
df_kategorier = df[ind_kategorier]

# a) 
display(df_aktiviteter)

# b) 
tillatt = ['Alle', 'Menn', 'Kvinner']
valgt_kjønn = input(f"Velg for hvilket kjønn dataene skal presenteres {tillatt}")
while valgt_kjønn not in tillatt:
    valgt_kjønn = input(f"Velg for hvilket kjønn dataene skal presenteres {tillatt}")

# Renser dataene og setter index blir aktivitetene eller kategoriene og henter ut dataserien for Tidsbruk
df_akt = df_aktiviteter[df_aktiviteter["Kjønn"]==valgt_kjønn]
df_akt.index = df_akt["Aktivitet"]
df_akt = df_akt["Tidsbruk"]

df_kat = df_kategorier[df_kategorier["Kjønn"]==valgt_kjønn]
df_kat.index = df_kat["Aktivitet"]
df_kat = df_kat["Tidsbruk"]

# Viser tabell med alle aktivitetene for det valgte kjønnet
display(df_akt)

# c) 
# Lager stolpe og sektordiagram for henholdsvis aktivitetene og for aktivitetskategoriene for det valgte kjønnet
plt.figure()
plt.title(f"Tidsbruk aktiviteter: {valgt_kjønn}")
df_akt.plot.bar()

plt.figure()
plt.title(f"Tidsbruk aktivitetskategorier: {valgt_kjønn}")
df_kat.plot.pie()
