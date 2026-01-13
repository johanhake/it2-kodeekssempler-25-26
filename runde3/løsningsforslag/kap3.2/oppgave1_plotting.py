import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x-3

x = np.linspace(0,20, 51)

plt.plot(x, f(x), color="orange")
plt.xlim(0,20)
plt.ylim(-10,40)
plt.xlabel("x")
plt.ylabel("y")

plt.show()                    
