# 1.6.1 a
data  = []
fortsett = True
while fortsett:
    tekst_inn = input('Skriv inn et heltall: ')
    if tekst_inn == '': fortsett = False
    if tekst_inn.isnumeric():
        data.append(tekst_inn)
with open('heltall.txt', mode='w') as fil:
    fil.write('\n'.join(data))

# Smidig IT-2 © TIP AS 2024