import pandas as pd
from IPython.display import display

df = pd.read_csv("titanic.csv", sep=",", encoding="utf-8")

display(df.head())