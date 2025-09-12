# Lag setninger med vilkårlige ord.
from random import randint, choice

fornavn = ['Kent', 'Lene', 'Mons']
beskrivelser = ['enestående', 'flott', 'god', 'herlig']

for navn in fornavn:
    beskrivelse = beskrivelser[randint(0, 3)]
    print(f'Hei {navn}, håper du får en {beskrivelse} kveld.')

# Bedre løsning:
for navn in fornavn:
    beskrivelse = choice(beskrivelser)
    print(f'Hei {navn}, håper du får en {beskrivelse} kveld.')

# Smidig IT-2 © TIP AS 2024