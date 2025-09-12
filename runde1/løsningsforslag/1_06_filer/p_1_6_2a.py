# 1.6.2 a
print('Sjekker filsignatur')
filnavn = input('Skriv inn filnavn: ')
with open(filnavn, mode='rb') as fil:
    signatur = fil.read(3)
    if signatur[:2]  == b'\xff\xd8':
        print(f'{filnavn} er en .jpg fil.')
    elif signatur  == b'ID3':
        print(f'{filnavn} er en .mp3 fil.')
    else:
        print(f'{filnavn} har ukjent filtype.')

# Smidig IT-2 © TIP AS 2024