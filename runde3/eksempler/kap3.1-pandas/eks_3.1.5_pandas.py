"""
### Pandas
[Pandas](https://pandas.pydata.org/) er et bibliotek for å manipulere og analysere tabeller. Det bruker egne objekter (datastrukturer), *Series* for endimensjonale tabeller og *DataFrame* for todimensjonale tabeller. *DataFrame* minner mye om et regneark eller en SQL-tabell med rader og kolonner. 

#### Lese inn DataFrame fra fil
Ofte vil vi lese inn dataene fra en fil med *pd.read_json()* eller *pd.read_csv()*, og *pandas* legger dataene inn i en *DataFrame*, gjerne med kolonneoverskrifter.

#### Lage en DataFrame fra lister av lister
Vi kan også opprette en *DataFrame* fra en liste med lister. Til å begynne med er radene og kolonnene angitt med indeksnummer, men vi kan gi dem navn med *df.index* og *df.columns*
"""

import pandas as pd

## Vi bruker display fra IPython istedenfor print!
from IPython.display import display

lst = [[ 1, 2, 3, 4],
       [ 5, 6, 7, 8],
       [ 9,10,11,12],
       [13,14,15,16]]
df = pd.DataFrame(lst)
display(df)
print()

## Endre på kolonne og rad navn
df.columns =['A','B','C','D']
df.index = ['Øst','Sør','Vest','Nord']
display(df)
print()

## Bruke info() til å få ut informasjon om kolonnene
df.info()

## Vi kan plukke ut verdier til enkelt kolonner ved å angi kolonnenavnene i en liste inne i en indeksoperator `[['A', 'C']]` og vi kan gi betingelser til hvilke rader vi vil ha med
BD = df[['B','D']]
display(BD)
print()

print(type(BD))
print()

B = df['B']
display(B)
print()

print(type(B))
print()

## Henter ut rader vars kolonne-verdi er større enn 5
A5 = df[df['A']>5]
display(A5)

## Henter ut rader vars kolonne-verdi er større enn 5 og så bare enkelt kolonner

A5BD = df[df['A']>5][['B','D']]
display(A5BD)

## Vi kan også plukke ut rader og kolonner med df.iloc (indeksnummer) og df.loc (navn)

display(df)
øst_vest_BD = df.iloc[([0,2],[1,3])]
display(øst_vest_BD)
print()

## Vi kan legge til en ny kolonne med utregninger med normal tilordning (=) og fjerne den med df.drop()

df['E']=df['A']*2
display(df)
print()

df = df.drop(columns="E")
display(df)
print()

## Skal vi legge til rader, lager vi først en *DataFrame* (rad) og så bruker vi *pd.concat()* til å legge til den, og skal vi fjerne dem kan vi bruke *df.drop()*

nyrad = pd.DataFrame([[22,24,26,28]], \
    columns=['A','B','C','D'], \
    index=['Nord-Vest'])
df = pd.concat([df,nyrad])
display(df)
print()

df = df.drop(index="Nord-Vest")
display(df)
print()