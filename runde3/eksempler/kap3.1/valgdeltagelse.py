import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("valgdeltagelse.txt", delimiter=";")

# a)
år = data[:,0]
deltagelse = data[:,1]

# b)
plt.plot(år, deltagelse)
plt.xlim(1940, 2030)
plt.ylim(70, 90)
plt.grid()
plt.title("Valgdeltagelse")
plt.show()

# c)
mer_enn_80 = deltagelse > 80
#print(år[mer_enn_80])
print("År med større valgdeltagelse enn 80 %")
#print(år[mer_enn_80].astype(int).astype(str))
print(", ".join(år[mer_enn_80].astype(int).astype(str)))

# join / split digresjon
# print(" | ".join(["H", "G", "K"]))
# print("Hei på deg din luring!".split(" "))

# d)
print(f"Det er {len(år[mer_enn_80])} år med valgdeltagelse mer enn 80 %.")
print(f"Det er {sum(mer_enn_80)} år med valgdeltagelse mer enn 80 %.")
