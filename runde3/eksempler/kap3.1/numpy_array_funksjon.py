import numpy as np
import matplotlib.pyplot as plt

tall = np.linspace(-5, 5, 101)
verdier = tall**2 + 5
verdier -= 2*tall

print(verdier)

def f(x):
    return x**2 -2*x + 5 

plt.plot(tall, f(tall))
plt.show()