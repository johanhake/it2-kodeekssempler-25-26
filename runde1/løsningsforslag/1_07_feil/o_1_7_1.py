# Lag setninger med vilkårlige ord.
from random import randint

fornavn = ['Kent','Lene,'Mons']
beskrivelser = ['enestående','flott','god','herlig']

for navn in fornavn:
     beskrivelse = beskrivelser[randint(1,4)]
    print(f'Hei {navn}, håper du får en {beskrivelse} kveld.')

# Smidig IT-2 © TIP AS 2024