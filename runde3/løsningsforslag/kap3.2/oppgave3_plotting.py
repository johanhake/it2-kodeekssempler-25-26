import matplotlib.pyplot as plt
import numpy as np

# Graf 1
xverdier = np.linspace(-5, 5, 21)
yverdier = 2*xverdier + 1
plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
xverdier = np.linspace(-5, 5, 21)
yverdier = xverdier**2 - 3
plt.subplot(2, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 3
xverdier = np.linspace(-3, 3, 21)
yverdier = 2**xverdier
plt.subplot(2, 2, 3)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 4
xverdier = np.linspace(-5, 5, 51)
yverdier = 3 / xverdier
plt.subplot(2, 2, 4)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()
