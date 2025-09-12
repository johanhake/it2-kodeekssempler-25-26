# Gitt listen tall = [10, 20, 30, 40, 50]
# a)	Skriv ut det første og siste elementet.
# b)	Skriv ut listen i reversert rekkefølge.
#       Hint: Bruk [::-1] for å skrive ut listen
#       i omvendt rekkefølge uten å endre den opprinnelige listen.
# c)	Endre det tredje elementet til 35 og skriv ut hele listen igjen.
tall = [10, 20, 30, 40, 50]
print(f'Første element: {tall[0]}')
print(f'Siste element: {tall[-1]}')
print(f'Reversert liste: {tall[::-1]}')
tall[2] = 35
print(f'Endret liste: {tall}')

# Smidig IT-2 © TIP AS 2024