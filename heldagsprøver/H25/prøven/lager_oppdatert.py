class Lager:
    def __init__(self):
        self.produkter = {}
        print('Lageret er opprettet')

    def innkjøp(self, navn: str, antall: int):
        if not isinstance(antall, int):
            raise TypeError('Antall må være et heltall')
        elif antall < 0:
            raise ValueError('Antall må være større enn 0')

        if navn in self.produkter:
            self.produkter[navn].antall += antall
        else:
            self.produkter[navn] = Produkt(navn, antall)
        print(f'Innkjøp av {antall} {navn} er gjennomført')

    def salg(self, navn, antall):
        if navn not in self.produkter:
            raise KeyError('Produktet finnes ikke på lageret')

        if antall > self.produkter[navn].antall:
            raise ValueError('Ikke nok varer på lager')

        self.produkter[navn].antall -= antall
        print(f'Salg av {antall} {navn} er gjennomført')

    def hent_beholdning(self, navn):
        return self.produkter[navn].antall

class Produkt:
    def __init__(self, navn, antall=0):
        self.navn = navn
        self.antall = antall

if __name__ == "__main__":
    lager = Lager()
    lager.innkjøp("Melk", 10)
    print(f'Antall Melk på lager: {lager.hent_beholdning("Melk")}')
    lager.salg("Melk", 7)
    print(f'Antall Melk på lager: {lager.hent_beholdning("Melk")}')
    lager.innkjøp("Melk", 5)
    print(f'Antall Melk på lager: {lager.hent_beholdning("Melk")}')