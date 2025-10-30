class Dyr:
    def __init__(self, navn):
        self.dyr = "dyr"
        self.navn = navn

    def hils(self):
        print(f'Hei, jeg heter {self.navn} og er en {self.dyr}.')


class Hund(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
        self.dyr = "hund"


class Katt(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
        self.dyr = "katt"


liste_med_dyr = [Hund('Hans')]
liste_med_dyr.append(Katt('Kristin'))
for dyr in liste_med_dyr:
    dyr.hils()

