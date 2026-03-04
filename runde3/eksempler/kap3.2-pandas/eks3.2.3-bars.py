import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display

aarstall = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]
arbeiderpartiet = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
hoyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

df = pd.DataFrame(zip(arbeiderpartiet, hoyre))
df.index = aarstall
df.columns = ["AP", "H"]
display(df)

df.plot.barh()
plt.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.title("Stortingsrepresentanter")
plt.show()  # Viser diagrammet
