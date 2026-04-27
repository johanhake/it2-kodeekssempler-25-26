from oppgave_2 import *

a = Turleder("a")
b = Medlem("b")
c = Medlem("c")
d = Medlem("d")
e = Medlem("e")


assert c.medlemsnr == 1003 # sjekker korrekt medlemsnr
assert e.medlemsnr == 1005 # sjekker korrekt medlemsnr

tur = Tur("Turmål",a)
assert tur.destinasjon == "Turmål"
assert isinstance(tur.turleder, Turleder)

# Melder på
tur.meld_på(b) 
tur.meld_på(c)
tur.meld_på(d)
tur.meld_på(e) 

assert len(tur.turdeltakere) == 4
assert tur.meld_på(Medlem("f")) 
assert isinstance(tur.info(), str) 

while tur.meld_på(Medlem("Jada")):
    pass

assert len(tur.turdeltakere) == tur.turleder.maks_deltakere 
assert not tur.meld_på(Medlem("Bada"))
