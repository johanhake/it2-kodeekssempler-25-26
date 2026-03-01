from bank import Kunde, Konto, Sparekonto

janne = Kunde("Janne")

assert janne.navn == "Janne"

assert len(janne.kontoer) == 0

jannes = janne.åpne_konto("sparing", 40_000)
jannek = janne.åpne_konto("konto", 4_000)

assert len(janne.kontoer) == 2

assert jannes.kontonr != jannek.kontonr, "Ikke like kontonr"
assert jannes.kontonr // 1000 > 0, "Fire siffer"
assert jannes.kontonr // 10000 == 0, "Ikke flere enn fire siffer"

assert jannes.uttak(10_000), "Har dekning"
assert not jannes.uttak(40_000), "Har ikke dekning"
assert jannes.saldo == 30_000, "Korrekt saldo"
assert jannes.antall_uttak == 1, "Antall uttak igjen"
jannes.uttak(5_000)
jannes.uttak(5_000)
jannes.uttak(5_000)
assert jannes.antall_uttak == 4, "Antall uttak igjen"
assert not jannes.uttak(5_000), "Kan ikke ta flere uttak"


