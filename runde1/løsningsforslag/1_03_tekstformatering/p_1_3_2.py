# Del 1
tekst = input('Skriv inn et heltall: ')

if tekst.isnumeric():
    tall = int(tekst)
    print(f'{tall} i titallsystemet er {tall:b} binært.')
else:
    print(f'{tekst} er ikke et heltall')

#Del 2
while True:
    tekst = input('Skriv inn et heltall: ')

    if tekst.isnumeric():
        tall = int(tekst)
        print(f'{tall} i titallsystemet er {tall:b} binært.')
    elif tekst == 'slutt':
        print('Takk for nå.')
        break
    else:
        print(f'{tekst} er ikke et heltall')

# Smidig IT-2 © TIP AS 2024