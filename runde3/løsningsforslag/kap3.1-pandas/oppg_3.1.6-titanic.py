import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv", sep=",", encoding="utf-8")

df.head()
print(f"1) Datasettet inneholder {len(df.index)} rader og {len(df.columns)} kolonner")
display(df.head())

print("2)")
display(df.head(3)[["sex", "age"]])

print("3)")
display(df.iloc[[9,29,19]])

print(f"4) De dyreste bilettene kostet: {df['fare'].max():.2f} £\n   og gjennomsnittsprisen var: {df['fare'][df['fare']>0].mean():.2f} £")

print("6) Antall barn, kvinner og menn")
display(df.groupby("who").count()["survived"])

print("8)")
df.groupby("who").count()["survived"].plot.bar()
plt.ylabel("Antall personer")

print("9) Hvem overlevde?")
for hvem, overlevde in df.groupby("who").mean(numeric_only=True)["survived"].items():
    print(f" {hvem:5} | {overlevde*100:.1f} %")

print("10) Prosent overlevde")
menn_3e_klass = df[(df["who"]=="man").values & (df["pclass"]==3).values]
print(f"Prosent av menn på 3e klasse som overlevde: {menn_3e_klass["survived"].mean()*100:.1f} %")

kvinner_1e_klass = df[(df["who"]=="woman").values & (df["pclass"]==1).values]
print(f"Prosent av kvinnene på 1e klasse som overlevde: {kvinner_1e_klass["survived"].mean()*100:.1f} %")

print("11) Overlevende per klasse")

overlevende = []
omkomne = []
for klasse in range(1,4):
    overlevende.append(sum((df["pclass"] == klasse).values & (df["survived"] == 1).values))
    
    omkomne.append(sum((df["pclass"] == klasse).values & (df["survived"] == 0).values))
    
to_bar = pd.DataFrame([overlevende, omkomne])
to_bar.index = ["Overlevende", "Omkomne"]
to_bar.columns = list(range(1,4))
plt.title("Antall overlevende og omkomne per klasse")
to_bar.plot.bar()