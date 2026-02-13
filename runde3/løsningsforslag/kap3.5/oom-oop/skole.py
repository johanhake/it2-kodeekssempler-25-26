class Elev:
    def __init__(self, navn: str):
        self.navn: str = navn 


class Klasse:
    def __init__(self, navn: str):
        self.navn = navn 
        self.elever = [] 

    def registrer_elev(self, elev: Elev) -> None:
        """Legg til elev i klassen."""
        self.elever.append(elev)

    def fjern_elev(self, elev: Elev) -> None:
        """Fjern elev fra klassen (ignorerer hvis ikke funnet)."""
        try:
            self.elever.remove(elev)
        except ValueError:
            pass

    def oversikt(self) -> str:
        """
        Viser en oversikt for denne klassen:
        - Klassenavn
        - Antall elever
        - Liste over elevnavn
        """
        elevnavn = "(ingen elever)"
        if self.elever:
            elevnavn = "  \n".join(e.navn for e in self.elever)
        
        print(f"Klasse: {self.navn}")
        print(f"Antall elever: {len(self.elever)}")
        print(elevnavn)

class Skole:
    def __init__(self, navn: str):
        self.navn = navn 
        self.klasser = []

    def registrer_klasse(self, klasse: Klasse) -> None:
        """Legg til klasse på skolen."""
        self.klasser.append(klasse)

    def fjern_klasse(self, klasse: Klasse) -> None:
        """
        Fjern klasse fra skolen, og fjern samtidig elevene i den klassen.
        (Elevene er en del av klassen, så vi tømmer listen for tydelighet.)
        """
        if klasse in self.klasser:
            # Tøm elevene i klassen i tråd med kravet
            klasse.elever.clear()
            self.klasser.remove(klasse)

    def oversikt(self) -> str:
        """
        Viser en oversikt for skolen:
        - Skolens navn
        - Antall klasser
        - Totalt antall elever
        """
        ant_klasser = len(self.klasser)
        
        ant_elever = 0
        for k in self.klasser:
            ant_elever += len(k.elever)
            
        print(f"Skole: {self.navn}")
        print(f"Antall klasser: {ant_klasser}")
        print(f"Antall elever: {ant_elever}")