import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2
plt.subplot(1, 2, 1)
plt.plot(xverdier, yverdier)
plt.xlim(0,20)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3
plt.subplot(1, 2, 2)
plt.plot(xverdier, yverdier)
plt.xlim(0,20)
plt.grid()

plt.show()
