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
    def __init__(self) -> None:
        ???

    def utfør(self, antall: int) -> list:
        ???
    
    def info(self) -> str:
        return f"{self.navn} er {self.alder} år og han deler ut gaver."

class Nissemor(Nisse):
    def __init__(self) -> None:
        ???

    def utfør(self) -> str:
        return "Grøt!!"
    
    def info(self) -> str:
        return f"{self.navn} er {self.alder} år og hun koker grøt."

class Arbeidsnisse(Nisse):
    # Klass-attributt. Et attributt som er lik for ALLE objekter. Da lagres det i klassen
    mulige_gaver = ["politibil", "lekebil", "dukke", "bamse", "leketåg", "sykkel", "servise"]

    def __init__(self, navn: str, alder: int) -> None:
        ???
    
    # Metode som er lik for alle objekter i en klasse. 
    # Kan bruke en klassemetode (men det tar vi i runde 3)
    def utfør(self) -> str:
        return ???

    def info(self) -> str:
        return f"{self.navn} er arbeidsnisse og er {self.alder} år."
    
class Juleverksted:
    def __init__(self, lokasjon) -> None:
        self.lokasjon = ???
        self.gaver = ???
        self.arbeidsnisser = ???
        self.far = ???
        self.mor = ???
        
    def legg_til_arbeidsnisse(self, nisse:Arbeidsnisse) -> None:
        self.arbeidsnisser.append(nisse)

    def produser(self) -> None:
        for nisse in self.arbeidsnisser:
            ???

    def vis_nisser(self) -> None:
        print(self.far.info())
        print(self.mor.info())
        for nisse in self.arbeidsnisser:
            ???

    def overfør_gaver_til_nissefar(self):
        self.far.gaver ???
        self.gaver = ???

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