# Gitt listen frukt = ['eple', 'appelsin', 'banan']
# a)	Legg til 'kiwi' på slutten av listen og skriv den ut.
# b)	Finn indeksen til 'appelsin' og erstatt 'appelsin' med 'plomme'
# c)	Fjern 'banan' fra listen ved å bruke verdien.
frukt = ['eple', 'appelsin', 'banan']
print(frukt)
frukt.append('kiwi')
print(frukt)
if 'appelsin' in frukt:
    frukt[frukt.index('appelsin')] = 'plomme'
print(frukt)
if 'banan' in frukt:
    frukt.remove('banan')
print(frukt)

# Smidig IT-2 © TIP AS 2024