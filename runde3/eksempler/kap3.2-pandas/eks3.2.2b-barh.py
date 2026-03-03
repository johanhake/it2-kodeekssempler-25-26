import matplotlib.pyplot as plt
import pandas as pd

reisemaate = ["Går", "Sykler", "Buss", "Moped", "Bil"]
antall = [5, 7, 10, 4, 3]

serie = pd.Series(antall, reisemaate)
serie.plot.barh()
#plt.barh(reisemaate, antall)
plt.title("Reisemåte til/fra skolen")
plt.grid(axis="x")
plt.show()
