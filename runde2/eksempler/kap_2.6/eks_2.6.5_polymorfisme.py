class Dyr:
    def __init__(self, navn: str) -> None:
        self.dyr = "dyr"
        self.navn = navn

    def hils(self) -> None:
        print(f'Hei, jeg heter {self.navn} og er en {self.dyr}.')

class Hund(Dyr):
    def __init__(self, navn: str) -> None:
        super().__init__(navn)
        self.dyr = "hund"
        
    def hils(self) -> None:
        print("Voff! ", end="")
        super().hils()

class Katt(Dyr):
    def __init__(self, navn: str) -> None:
        super().__init__(navn)
        self.dyr = "katt"

    def hils(self) -> None:
        print("Voff! ", end="")
        super().hils()


class Sau(Dyr):
    def __init__(self, navn: str) -> None:
        super().__init__(navn)
        self.dyr = "sau"

    def hils(self) -> None:
        print('Bææ! ', end='')
        super().hils()

liste_med_dyr = []
liste_med_dyr.append(Hund('Hans'))
liste_med_dyr.append(Katt('Kristin'))
liste_med_dyr.append(Sau('Sigurd'))

for dyr in liste_med_dyr:
    dyr.hils()

for dyr in liste_med_dyr:
    if isinstance(dyr, Hund):
        print('Voff!')
    elif isinstance(dyr, Katt):
        print('Mjau!')
    elif isinstance(dyr, Sau):
        print('Bææ!')
        
class Mus(Dyr):
    def __init__(self, navn: str) -> None:
        super().__init__(navn)
        self.dyr = "mus"

dyr = Mus('Mikke')
dyr.hils()
