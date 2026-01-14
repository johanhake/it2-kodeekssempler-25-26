import numpy as np
import matplotlib.pyplot as plt

tall1 = np.array([-1, 1, 3, 5, 9])
tall2 = np.array([-2, 2, 6, 10, 14])

# Verdi tabell zip og enumerate
# for i, (t1, t2) in enumerate(zip(tall1, tall2)):
#     print(f"{i+1} | {t1:2} | {t2:2}")

# def f(x):
#     return x**2 -2*x + 5

# x = np.linspace(-5,5, 11)
# print(f(x))
# plt.plot(x,f(x))
# plt.show()

# print(tall1[2:])
# print(tall2[:3])
# print(tall1[::2])
# print(tall1[1:]-tall1[:-1])

# # Viser grafen en funksjon 
# x = tall1
# y = tall2
# print((y[1:]-y[:-1])/(x[1:]-x[:-1]))
# plt.plot(x, y)
# plt.show()

# Bruker boolske arrays til å hente ut verdier fra numpy array
x = tall1
y = tall2
print(x)
print(y)
ind = np.array([True, False, True, True, False])
print(ind)
print(x[ind])
print(y[ind])
print(x > 2)
print(y[x > 2])

