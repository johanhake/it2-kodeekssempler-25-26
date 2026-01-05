from lager import Lager, Produkt
# Normal bruk
lager = Lager()

assert isinstance(lager, Lager), "Er et Lager"
assert lager.produkter == {}, "Tom ordbok"

# tester innkjøp av ny vare
lager.innkjøp("Melk", 10)
assert "Melk" in lager.produkter, "Melk er kjøpt inn"
assert lager.produkter["Melk"].antall == 10, "Vi har 10 Melk"

# tester innkjøp eksisterende vare
lager.innkjøp("Melk", 10)
assert lager.produkter["Melk"].antall == 20, "Øker beholdningen til 20"

# tester salg
lager.salg("Melk", 7)
assert lager.produkter["Melk"].antall == 13, "Salg av produkt"

# tester hent beholdning
assert lager.hent_beholdning("Melk") == 13, "Hent beholdning"


