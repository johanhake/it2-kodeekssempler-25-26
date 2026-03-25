import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

df = pd.read_csv("Global YouTube Statistics.csv")
df_country = df.groupby(["Country"]).count()

# a) De ti lendene med fleste de fleste appene
land_10_fleste = df_country.sort_values(["rank"], ascending=False).index[:10]

print("De 10 landene som har flest YT kanaler")
for i, land in enumerate(land_10_fleste):
    print(f"{i+1:2} | {land}")

df_country_mean = df.groupby(["Country"]).mean(numeric_only=True).loc[land_10_fleste, ["subscribers", "video views"]]

display(df_country_mean)

# Burte funker men får feil i den siste kolonnen. Det er for at største tallet for en int er ~2B
# Den bruker 32 bit som betyr 2^32~4.3B og når det kan være både negative og positive tall så blir det
# 2^32/2~2.1B
display(df_country_mean.round(0).astype(int))

# Bruker 'Int64' som type istedenfor. Da funker det!!
display(df_country_mean.round(0).astype("Int64"))

# Skalerer dataene slik at de gjør seg bedre i en graf
df_country_mean["subscribers"] = df_country_mean["subscribers"]/1e6
df_country_mean["video views"] = df_country_mean["video views"]/1e9
axes = df_country_mean.plot.bar(subplots=True)
axes[0].set_ylabel("Milioner")
axes[1].set_ylabel("Miliarder")
plt.show()