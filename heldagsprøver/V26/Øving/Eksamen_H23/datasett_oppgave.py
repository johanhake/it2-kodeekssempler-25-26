from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Global YouTube Statistics.csv", encoding="utf-8",sep=",")

display(df.head())

land_med_flest_yt = df.groupby("Country").count()["rank"].sort_values(ascending=False).index[0:10]

print("Land med flest YT kanaler")
for i, land in enumerate(land_med_flest_yt):
    print(f"{i+1:2} | {land}")
    
display(df.groupby("Country").mean(numeric_only=True)[["subscribers", "video views"]].loc[land_med_flest_yt])