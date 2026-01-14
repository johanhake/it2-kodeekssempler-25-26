import matplotlib.pyplot as plt

partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
farger = ["#f58c68", "#004281", "#3396d2", "#d2bc2a", "#25a23c", "#5d0008", "#90cc93", "#d34d2f", "#005245", "#f69465"]  # Hentet herfra https://www.ssb.no/valg/faktaside/valg
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]

plt.pie(representanter, labels=partiforkortelser, colors=farger, wedgeprops=dict(edgecolor='black', linewidth=0.5))
plt.show()
