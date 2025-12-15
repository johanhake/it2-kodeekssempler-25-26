import numpy as np

# leser inn fil med data og lager 2D array med heltall
data = np.loadtxt("rektangler.txt", delimiter=",", dtype=int)

#print(data)

# Henter ut første og andre kolonnen
bredder = data[:,0]
lengder = data[:,1]

#print(bredder, lengder)

areal = bredder*lengder
print(areal)

print("a)", bredder[1::2]*lengder[1::2])
print("b)", bredder[1::2]*lengder[::2])
print("c)", bredder*lengder[::-1])