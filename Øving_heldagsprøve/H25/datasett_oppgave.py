import csv

with open("friluftsaktiviteter.csv") as fil:
    data = csv.reader(fil, delimiter=";")
    
    fylker = next(data)[1:]
    aktiviteter = []
    antall_aktiviter = []
    
    for d in data:
        aktiviteter.append(d[0])
        antall = []
        
        # Går igjennom alle tallene i listen
        for tall in d[1:]:
            antall.append(int(tall))
        
        antall_aktiviter.append(antall)
        
        # Bruk av listcomprehension
        #antall_aktiviter.append([int(tall) for tall in d[:1]])
    
    print(f"Antall fylker: {len(fylker)}")
    print(f"Antall aktiviteter: {len(aktiviteter)}\n")
    
    # Summerer aktivitetene
    sum_aktiviteter = []
    for antall in antall_aktiviter:
        sum_aktiviteter.append(sum(antall))
        
    # Skriver ut aktivitetene i en tabell
    for i in range(len(aktiviteter)):
        aktivitet = aktiviteter[i]
        antall = sum_aktiviteter[i]
        print(f"{aktivitet:60} : {antall}")
    
    # Brukeren velger fylke:
    print("\n")
    for i in range(len(fylker)):
        print(f"{i+1:2} : {fylker[i]}")
    
    fylke_indeks = int(input("Velg fylke: "))-1
    
    print(f"\n\nViser aktivteter for: {fylker[fylke_indeks]}")
    
    # Vise per fylke:
    for i, aktivitet in enumerate(antall_aktiviter):
        print(f"{aktivitet[fylke_indeks]:4} | {aktiviteter[i]}")
    
    # Sorterer nå:
    # Lager en liste med lister som kan sorteres:
    # [[552, "Gåtur i parker..."],
    #  [429, "Fottur i fjell, ..."],
    #  [151, "Sykkeltur"],
    #  ...
    #  [32,  "Deltatt i organiserte ..."]]
    sorterte_aktiviteter = []
    for i in range(len(aktiviteter)):
        # Henter ut aktiviteten og antallet tilhørende fylket
        aktivitet = aktiviteter[i]
        antall = antall_aktiviter[i][fylke_indeks]

        sorterte_aktiviteter.append([antall, aktivitet])
    
    # Funksjon som henter ut første elementet
    def første(e):
        return e[0]
    
    # Utfører selve sorteringen
    sorterte_aktiviteter.sort(reverse=True, key=første)
    
    print(f"\n\nViser sorterte aktivteter for: {fylker[fylke_indeks]}")
    for antall, aktivitet in sorterte_aktiviteter:
        print(f"{antall:4} | {aktivitet}")
    