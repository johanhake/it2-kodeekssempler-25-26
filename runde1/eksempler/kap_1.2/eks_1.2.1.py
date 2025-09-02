kmpt_per_knop = 1.852
avstand_i_km = float(input('Oppgi avstand i km: '))
fart_i_knop  = int(input('Oppgi fart i knop: '))
fart_i_kmpt  = fart_i_knop * kmpt_per_knop
flytid       = avstand_i_km / fart_i_kmpt
print(flytid)