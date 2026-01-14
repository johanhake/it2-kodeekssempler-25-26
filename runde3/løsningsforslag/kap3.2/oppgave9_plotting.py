import matplotlib.pyplot as plt
import numpy as np

aarstall = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]
arbeiderpartiet = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
hoyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

plt.figure(figsize=(10, 5))  # Angir dimensjoner for figureobjektet
y = np.arange(10)
plt.barh(y+0.2, arbeiderpartiet, height=0.4, label="AP")  # Stolpediagram AP
plt.barh(y-0.2, hoyre, height=0.4, label="H")  # Stolpediagram H
plt.yticks(y, aarstall)  # Akseverdier
plt.legend()  # Beskrivelse
plt.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.title("Stortingsrepresentanter")
plt.show()  # Viser diagrammet
