import matplotlib.pyplot as plt

utdanningsprogram = [
    "Bygg- og anleggsteknikk",
    "Elektro og datateknologi",
    "Helse- og oppvekstfag",
    "Naturbruk",
    "Restaurant- og matfag",
    "Teknologi- og industrifag",
    "Håndverk, design og produktutvikling",
    "Frisør, blomster, interiør og eksponeringsdesign",
    "Informasjonsteknologi og medieproduksjon",
    "Salg, service og reiseliv"
]

antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

plt.figure(figsize=(10, 5))  # Angir dimensjoner for figureobjektet
plt.pie(antallJenter, labels=utdanningsprogram, wedgeprops={"linewidth": 1, "edgecolor": "white"})
plt.show()
