import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**3 - x**5

format = ["-b", "-.r", "--g", ":y"]
antall_punkter = [5, 10, 20, 50]

for fo, p in zip(format, antall_punkter):
    x = np.linspace(-2, 2, p)
    plt.plot(x, f(x), fo) 
    
plt.show()
