venner = ['Ole', 'Dole', 'Doffen', 'Dole', 'Dolly']
print(venner)
navn = 'doffen'
if navn in venner:
    indeks = venner.index(navn)
    print(f'Første forekomst av {navn} er i posisjon {indeks}')
else:
    print(f'{navn} forekommer ikke i venner-listen.')
    
navn = 'dole'
antall = venner.count(navn)
print(f'{navn} forekommer {antall} ganger i venner-listen.')