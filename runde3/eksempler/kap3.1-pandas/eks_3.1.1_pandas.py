import pandas as pd
from IPython.display import display

lst = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12], [13,14,15,16]]
df = pd.DataFrame(lst)
df.columns = ["A", "B", "C", "D"]
df.index = ["øst", "sør", "vest", "nord"]
df.info()
display(df)

# Henter ut kolonner og begrense data for rader
display(df["B"])
display(df[["B", "D"]])
display(df[df["A"]>5][["B", "D"]])

# Henter ut rader per index og navn
display(df)
display(df.iloc[[0,2], [1, -1]])
display(df.loc[["øst", "vest"], ["B", "D"]])

# Ny kolonne
df["E"] = df["A"]*2
display(df)
df_uten_E = df.drop(columns="E")
display(df)
display(df_uten_E)