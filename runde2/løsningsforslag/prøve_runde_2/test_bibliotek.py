from bibliotek import *

bok1 = Bok("Harry Potter", "JK Rowlings")
bok2 = Bok("Ringenes Herre", "JRR Tolkien")
bok3 = Bok("Jada", "Bada")

utlåner1 = Låner()
utlåner2 = Låner()

assert bok1.tittel == "Harry Potter", "Sjekker tittel på bok"
assert bok1.forfatter == "JK Rowlings", "Sjekker forfatter til bok"
assert bok2.tittel == "Ringenes Herre", "Sjekker tittel på bok"
assert bok2.forfatter == "JRR Tolkien", "Sjekker forfatter til bok"

assert utlåner1.lånerID != utlåner2.lånerID, "LånerID er unike"

assert len(utlåner1.lånte_bøker) == 0, "Låner starter med null lånte bøker"

utlåner1.lån_bok(bok1)
utlåner1.lån_bok(bok2)

assert len(utlåner1.lånte_bøker) == 2, "Låner har lånt to bøker"

utlåner1.lån_bok(bok1)
utlåner2.lån_bok(bok2)
utlåner2.lever_tilbake_bok(bok2)

assert len(utlåner1.lånte_bøker) == 2, "Låner har fortsatt lånt to bøker"

utlåner1.lever_tilbake_bok(bok2)

assert len(utlåner1.lånte_bøker) == 1, "Låner har levert tilbake en bok"

print("Allt vel!")

