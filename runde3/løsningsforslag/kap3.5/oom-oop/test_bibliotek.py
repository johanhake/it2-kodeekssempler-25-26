from bibliotek import Bibliotek, FysiskBok, EBok

bib = Bibliotek()
e = FysiskBok('Python 101', 'Guido', 150)
f = EBok('Python 102', 'Guido', 25)
g = FysiskBok('Python 103', 'Guido', 250)

bib.registrer(e)
bib.registrer(f)
bib.registrer(g)

assert len(bib.bøker) == 3
assert bib.søk('Python 101').forfatter == "Guido"
assert bib.søk('Python 102').størrelse == 25
assert bib.søk('Jada') is None

bib.oversikt()

