def tall_spill(tall):
    while True:
        
        # Logikk:
        # 1) Gjør om tallet til str
        # 2) Sorter str stigende eller synkende -> resultat er en liste med str-verdier
        # 3) Sett sammen disse verdier med tekst = "".join(liste)
        # 4) Gjør om tekst til tall med int(tekst)
        stigende_tall = int("".join(sorted(str(tall))))
        synkende_tall = int("".join(sorted(str(tall), reverse=True)))
        
        nytt_tall = synkende_tall-stigende_tall
        
        print(f"{synkende_tall:4} - {stigende_tall:4} = {nytt_tall:4}")
        
        if tall == nytt_tall:
            break
        
        tall = nytt_tall
        
tall_spill(3142)
        
    
    


