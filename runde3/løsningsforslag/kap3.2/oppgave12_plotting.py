import matplotlib.pyplot as plt
import numpy as np

jentebarn = np.random.normal(3.5, 0.5, 100)
guttebarn = np.random.normal(3.8, 0.5, 100)
bins = np.arange(0.5, 6.5, 0.5)

plt.figure()
plt.hist(jentebarn, bins=bins, edgecolor="black")
plt.xlabel("Fødselsvekt (kg)")
plt.ylabel("Antall")

plt.figure()
plt.hist(guttebarn, bins=bins, edgecolor="black")
plt.xlabel("Fødselsvekt (kg)")
plt.ylabel("Antall")

plt.show()
