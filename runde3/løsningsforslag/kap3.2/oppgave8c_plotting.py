import matplotlib.pyplot as plt

reisemaate = ["Går", "Sykler", "Buss", "Moped", "Bil"]
antall = [5, 7, 10, 4, 3]

plt.bar(reisemaate, antall, width=0.4, color="pink", edgecolor="darkblue", zorder=2)
plt.title("Reisemåte til/fra skolen")
plt.grid(axis="y", zorder=1)
plt.show()
