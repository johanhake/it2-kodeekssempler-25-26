import matplotlib.pyplot as plt

land = ["Kina", "Japan", "Tyskland", "USA", "Sør-Korea", "India", "Spania", "Mexico", "Brasil", "England"]
antall = [24420744, 7873886, 5746808, 3934357, 3859991, 3677605, 2354117, 1993168, 1778464, 1722698]

plt.barh(land, antall)
plt.title("Antall biler produsert i 2016")
plt.grid(axis="x")
plt.show()
