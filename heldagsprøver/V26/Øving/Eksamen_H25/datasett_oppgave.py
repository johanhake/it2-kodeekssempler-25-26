from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Elever-fag.csv", encoding="iso8859-1",sep=",")

display(df)

