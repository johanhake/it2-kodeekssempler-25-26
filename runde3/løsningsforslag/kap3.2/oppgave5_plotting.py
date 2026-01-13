import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(1, 10, 10)
for a in range(1, 6):
    plt.plot(xverdier, a*xverdier+3, label=f"a={a}")
plt.ylim(0,60)
plt.grid()
plt.legend()
plt.show()
