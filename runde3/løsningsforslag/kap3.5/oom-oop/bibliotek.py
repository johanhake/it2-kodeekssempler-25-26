class Bok:
    def __init__(self, tittel, forfatter):
        self.tittel = tittel
        self.forfatter = forfatter

    def vis(self):
        print(f"{self.tittel} av {self.forfatter}")

class FysiskBok(Bok):
    def __init__(self, tittel, forfatter, antall_sider):
        super().__init__(tittel, forfatter)
        self.antal_side = antall_sider

class EBok(Bok):
    def __init__(self, tittel, forfatter, størrelse):
        super().__init__(tittel, forfatter)
        self.størrelse = størrelse

class Bibliotek:
    def __init__(self):
        self.bøker = []

    def registrer(self, bok:Bok):
        if isinstance(bok, Bok):
            self.bøker.append(bok)
        else:
            print("Kan bare registrere objekter som er Bok.")

    def søk(self, tittel:str):
        for b in self.bøker:
            if b.tittel == tittel:
                return b
        return None
    
    def oversikt(self):
        ebøker = [b for b in self.bøker if isinstance(b, EBok)]
        fysiske_bøker = [b for b in self.bøker if isinstance(b, FysiskBok)]
        if ebøker:
            print("\nEbøker:")
            for b in ebøker:
                b.vis()
        
        if fysiske_bøker:
            print("\nFysiske bøker:")
            for b in fysiske_bøker:
                b.vis()
                

