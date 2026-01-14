import matplotlib.pyplot as plt

reisemaate = ["Går", "Sykler", "Buss", "Moped", "Bil"]
antall = [5, 7, 10, 4, 3]

plt.barh(reisemaate, antall)
plt.title("Reisemåte til/fra skolen")
plt.grid(axis="x")
plt.show()
