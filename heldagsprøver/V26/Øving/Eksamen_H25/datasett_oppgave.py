from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Elever-fag.csv", encoding="utf-8",sep=",")

# Henter alle fagområdene
fagområden = list(set(df["Fagomraadenavn"]))

# Oppgave a)
df_fagområden = df.groupby("Fagomraadenavn").sum()
display(df_fagområden[["2022-23","2023-24","2024-25"]])

# Oppgave b)
print(", ".join(fagområden))
valgt_fagområde = input("Skriv inn et fagområde: ")
while valgt_fagområde not in fagområden:
    valgt_fagområde = input("Skriv inn et fagområde: ")

df_valgt = df[df["Fagomraadenavn"]==valgt_fagområde].copy()
display(df_valgt[["Opplaeringsfagnavn", "2022-23","2023-24","2024-25"]])

# Oppgave c)
# Bruker dataframe fra valgt fagområde for videre beregninger
# Finner absolutt og relativ (prosentvis) forskjell
df_valgt["diff-22-24"]=df_valgt["2024-25"]-df_valgt["2022-23"]
df_valgt["prosent-diff-22-24"] = (df_valgt["diff-22-24"]/df_valgt["2022-23"]*100).round(1)

# Sorterer informasjonen
abs_sort = df_valgt.sort_values("diff-22-24")
prosent_sort = df_valgt.sort_values("prosent-diff-22-24")

# Henter ut første eller siste element fra tabellen og viser fagnavnet og verdien på oppgang (nedgang)
print("Størst absolutt oppgang (minst nedgang)", abs_sort.iloc[-1]["Opplaeringsfagnavn"], abs_sort.iloc[-1]["diff-22-24"])
print("Størst absolutt nedgang (minst oppgang)", abs_sort.iloc[0]["Opplaeringsfagnavn"], abs_sort.iloc[0]["diff-22-24"])
print("Størst prosentvise oppgang (minst nedgang)", prosent_sort.iloc[-1]["Opplaeringsfagnavn"], prosent_sort.iloc[-1]["prosent-diff-22-24"], "%")
print("Størst prosentvise nedgang (minst oppgang)", prosent_sort.iloc[0]["Opplaeringsfagnavn"], prosent_sort.iloc[0]["prosent-diff-22-24"], "%")
