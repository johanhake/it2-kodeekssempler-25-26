from hund import Hund

h1 = Hund(7, 15)

for _ in range(8):
    h1.spring()
    print(h1.hent_vekt())

for mat in [1,3,5,4]:
    h1.spis(mat)
    print(h1.hent_vekt())
