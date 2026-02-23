## For å vise *sortering* og *gruppering* leser vi først inn et datasett fra fil. **homes.csv**, *Home sale statistics. Fifty home sales, with selling price, asking price, living space, rooms, bedrooms, bathrooms, age, acreage, taxes. There is also an initial header line.*

import pandas as pd
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv'
df = pd.read_csv(url)

## Vi bruker display fra IPython istedenfor print!
from IPython.display import display

display(df)

## Rydde opp i kolonnenavn
display(df.columns)
df.columns= [x.strip().replace('"','') for x in df.columns]
display(df.columns)

## For å finne de tre dyreste hjemmene, kan vi bruke *df.sort_values* og *df.head()*
sortert = df.sort_values('Sell',ascending=False).head(3)
display(sortert)
print()

## Vi kan også sortere etter flere kolonner ved hjelp av lister: 
## 'Rooms' i synkende rekkefølge og 'Age' i stigende rekkefølge

sortert = df.sort_values(['Rooms','Age'],ascending=[False,True])
display(sortert)
print()

## For å finne gjennomsnittsprisen for hjemmene gruppert etter antall rom kan vi bruke *df.groupby()* og *df.mean()*. Hvis noen av kolonnene inneholder noe annet enn numeriske verdier, må vi bruke numeric_only = True

mean_rooms = df.groupby(df['Rooms']).mean(numeric_only=True)
display(mean_rooms)
print()


## Det finnes flere ulike matematiske operasjoner vi kan bruke, mean, min, max, osv. Her bruker vi *min* til å vise den billigste salgsprisen gruppert etter antall rom.
min_rooms = df[['Rooms','Sell']].groupby(df['Rooms']).min()
display(min_rooms)
print()