farger = ['rød', 'oransje', 'gul', 'grønn', 'blå', 'indigoblå', 'lilla']

try:
    indeks = int(input('Velg et tall fra 1 til 7: ')) - 1
except ValueError:
    print('Du må skrive inn et heltall.')
    exit()  # Avslutter programmet

try:
    print(f'Flott! Du valgte {farger[indeks]}.')
except IndexError:
    # NB: Tillater også tall fra 0 til -6
    print('Du må skrive inn et tall mellom 1 og 7.')

# Smidig IT-2 © TIP AS 2024
