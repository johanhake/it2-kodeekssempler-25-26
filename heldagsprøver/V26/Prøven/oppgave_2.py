from random import randint

neste_medlemsnr = 1001
class Medlem:
    def __init__(self, navn:str):
        if not isinstance(navn, str):
            #raise TypeError(f"Forventet en 'str' som verdi for 'navn' fikk {type(navn)}")
            print(f"Forventet en 'str' som verdi for 'navn' fikk {type(navn)}")
            return
        global neste_medlemsnr
        self.medlemsnr = neste_medlemsnr
        neste_medlemsnr += 1
        self.navn = navn

class Turleder(Medlem):
    def __init__(self, navn:str):
        super().__init__(navn)
        self.min_deltakere = randint(2,5)
        self.maks_deltakere = randint(10,20)

class Tur:
    def __init__(self, destinasjon:str, turleder:Turleder):
        if not isinstance(destinasjon, str):
            #raise TypeError(f"Forventet en 'str' som verdi for 'destinasjon' fikk {type(destinasjon)}")
            print(f"Forventet en 'str' som verdi for 'destinasjon' fikk {type(destinasjon)}")
            return 
        
        if not isinstance(turleder, Turleder):
            #raise TypeError(f"Forventet en 'Turleder' som verdi for 'turleder' fikk {type(turleder)}")
            print(f"Forventet en 'Turleder' som verdi for 'turleder' fikk {type(turleder)}")
            return 

        self.destinasjon = destinasjon
        self.turleder = turleder
        self.turdeltakere = []
    
    def meld_på(self, turgåer: Medlem):
        if isinstance(turgåer, Medlem):
            if len(self.turdeltakere) < self.turleder.maks_deltakere:
                self.turdeltakere.append(turgåer)
                print(f"{turgåer.navn} har blitt påmeldt til turen.")
                return True
            else:
                print(f"Beklager {turgåer.navn}! Turen er desverre full.")
                return False
        else:
            #raise TypeError(f"Forventet en 'Medlem' som verdi for 'turgåer' fikk {type(turgåer)}")
            print((f"Forventet en 'Medlem' som verdi for 'turgåer' fikk {type(turgåer)}"))
            return False
        
    def info(self):
        melding = f"\nTur til {self.destinasjon} med {self.turleder.navn} som leder\n"
        n = len(self.turdeltakere)
        skille = "-"*(len(melding)-1)+"\n"
        melding += skille
        if n < self.turleder.min_deltakere:
            melding += "Turen trenger flere deltakere for å starte!\n"
        elif n == self.turleder.maks_deltakere:
            melding += "Turen er full!\n"
        else:
            melding += "Turen er åpen for påmeldinger!\n"
        
        if n > 0:
            melding += "\nPåmeldte til turen\n"
            melding += skille
            for i, t in enumerate(self.turdeltakere):
                melding += f"{i+1:2} | {t.navn}\n"
        return melding

if __name__ == "__main__":
    tl = Turleder("Leder")
    tur = Tur("Sverige",tl)
    n = 65
    deltaker = Medlem(chr(n)*5)
    while tur.meld_på(deltaker):
        n += 1
        deltaker = Medlem(chr(n)*5)
    
    print(tur.info())