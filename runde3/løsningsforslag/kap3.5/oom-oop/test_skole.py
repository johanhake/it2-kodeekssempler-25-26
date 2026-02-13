from skole import Skole, Klasse, Elev

# Oppsett
skole = Skole("VGS Ski")
klasse_1a = Klasse("1A")
klasse_1b = Klasse("1B")

# Registrer klasser
skole.registrer_klasse(klasse_1a)
skole.registrer_klasse(klasse_1b)

assert len(skole.klasser) == 2

# Registrer elever i 1A
ola = Elev("Ola")
kari = Elev("Kari")
klasse_1a.registrer_elev(ola)
klasse_1a.registrer_elev(kari)

assert len(klasse_1a.elever) == 2
#assert "Antall elever: 2" in klasse_1a.oversikt()
#assert "Ola" in klasse_1a.oversikt() and "Kari" in klasse_1a.oversikt()

# Registrer elever i 1B
lise = Elev("Lise")
petter = Elev("Petter")
johan = Elev("Johan")
klasse_1b.registrer_elev(lise)
klasse_1b.registrer_elev(petter)
klasse_1b.registrer_elev(johan)

assert len(klasse_1b.elever) == 3

# Skole-oversikt (totalt)
oversikt_forr = skole.oversikt()

# Fjern én elev fra 1A
klasse_1a.fjern_elev(ola)
assert len(klasse_1a.elever) == 1
#assert "Antall elever: 1" in klasse_1a.oversikt()

# Prøver å fjerne elev fra 1B som ikke går der!
try:
    klasse_1b.fjern_elev(ola)
except: 
    pass
assert len(klasse_1b.elever) == 3

# Fjern klassen 1B (elevene i 1B skal også fjernes)
skole.fjern_klasse(klasse_1b)
assert len(skole.klasser) == 1
# 1B-elevene fjernes når klassen fjernes (liste tømmes)
assert len(klasse_1b.elever) == 0

# Ny totaloversikt
oversikt_etter = skole.oversikt()

