from random import choice

class Nisse:
    def __init__(self, navn:str, alder:int) -> None:
        self.navn = navn
        self.alder = alder

    def info(self) -> str:
        return f"{self.navn} er {self.alder} år."

    def utfør(self):
        raise NotImplementedError()
    
class Nissefar(Nisse):
    def __init__(self, alder) -> None:
        super().__init__("Nissefar", alder)
        self.gaver = []

    def utfør(self, antall: int) -> list:
        if len(self.gaver) < antall:
            print("Ikke nok gaver!")
        else:
            # List comprehension
            # return [self.gaver.pop() for i in range(antall)]
            ret = []
            for i in range(antall):
                ret.append(self.gaver.pop())
            
            return ret
            
    
    def info(self) -> str:
        return f"{self.navn} er {self.alder} år og han deler ut gaver."

class Nissemor(Nisse):
    def __init__(self, alder) -> None:
        super().__init__("Nissemor", alder)

    def utfør(self) -> str:
        return "Grøt!!"
    
    def info(self) -> str:
        return f"{self.navn} er {self.alder} år og hun koker grøt."

class Arbeidsnisse(Nisse):
    # Klass-attributt. Et attributt som er lik for ALLE objekter. Da lagres det i klassen
    mulige_gaver = ["politibil", "lekebil", "dukke", "bamse", "leketåg", "sykkel", "servise"]

    # Metode som er lik for alle objekter i en klasse. 
    # Kan bruke en klassemetode (men det tar vi i runde 3)
    def utfør(self) -> str:
        return choice(["politibil", "lekebil", "dukke", "bamse", "leketåg", "sykkel", "servise"])

    def info(self) -> str:
        return f"{self.navn} er arbeidsnisse og er {self.alder} år."
    
class Juleverksted:
    def __init__(self, lokasjon) -> None:
        self.lokasjon = "Nordpolen"
        self.gaver = []
        self.arbeidsnisser = []
        self.far = Nissefar(150)
        self.mor = Nissemor(145)
        
    def legg_til_arbeidsnisse(self, nisse:Arbeidsnisse) -> None:
        self.arbeidsnisser.append(nisse)

    def produser(self) -> None:
        for nisse in self.arbeidsnisser:
            self.gaver(nisse.utfør())

    def vis_nisser(self) -> None:
        print(self.far.info())
        print(self.mor.info())
        for nisse in self.arbeidsnisser:
            print(nisse.info())

    def overfør_gaver_til_nissefar(self):
        
        self.far.gaver = self.gaver
        self.gaver.clear()
        
        
        self.far.gaver = self.gaver.copy()
        
        self.far.gaver.extend(self.gaver)
        
        for gave in self.gaver:
            self.far.gaver.append(gave)
        
        self.gaver.clear()

if __name__ == "__main__":
    verksted = Juleverksted("Norpolen")
    verksted.vis_nisser()
    verksted.legg_til_arbeidsnisse(Arbeidsnisse("Hans", 78))
    verksted.legg_til_arbeidsnisse(Arbeidsnisse("Jakob", 70))
    verksted.legg_til_arbeidsnisse(Arbeidsnisse("Emily", 56))

    print()
    verksted.vis_nisser()

    print()
    print(verksted.gaver)
    verksted.produser()
    print(verksted.gaver)
    verksted.produser()
    verksted.produser()
    print(verksted.gaver)
    print(verksted.far.gaver)
    verksted.overfør_gaver_til_nissefar()
    print(verksted.gaver)
    print(verksted.far.gaver)
    print(verksted.far.utfør(4))
    print(verksted.far.gaver)
    print(verksted.mor.utfør())