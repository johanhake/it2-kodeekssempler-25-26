print('Når du er ferdig med å skrive inn tall,')
print('kan du trykke Enter uten å skrive noe.')
antall_tall = 0
while True:
    tekst_inn = input('Skriv inn et helttall: ')
    tall = int(tekst_inn)
    print('Du skrev inn {tall}')
    antall_tall += 1

print(f'Du skrev inn {antall_tall} tall.')
print('Takk for nå')