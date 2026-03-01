from IPython.display import display
import pandas as pd

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv'
df = pd.read_csv(url)
display(df)

df.columns = [navn.strip().replace('"', '') for navn in df.columns]

display(df.head())

# Sortere etter ulike kolonner
display(df.sort_values("Sell", ascending=False).head(3))

display(df.sort_values(["Rooms", "Age"], ascending=[False, True]))

# Gruppere data ved group_by finner gjennomsnittet til alle verdier gruppert etter rom
print(df.groupby(df["Rooms"]).mean()["Sell"])