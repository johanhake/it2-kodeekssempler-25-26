from random import randint

antall_kontonr = 0

class Kunde:
    def __init__(self, navn:str):
        self.navn = navn
        self.kontoer = {}

    def åpne_konto(self, type:str, beløp:float=0.):
        if type == "sparing":
            konto = Sparekonto(beløp)
        else:
            konto = Konto(beløp)

        self.kontoer[konto.kontonr] = konto

        return konto
    
class Konto:
    def __init__(self, innskudd:float):
        global antall_kontonr
        self.kontonr = 1000 + antall_kontonr
        antall_kontonr += 1
        self.saldo = innskudd

    def innskudd(self, beløp:float)->None:
        if beløp < 0:
            print("Beløp må være større enn 0")
        else:
            self.saldo += beløp

    def uttak(self, beløp:float)->bool:
        if beløp < 0:
            print("Beløp må være større enn 0")
            return False
        elif self.saldo - beløp < 0:
            print(f"Uttaks beløp må være mindre enn saldo på {self.saldo} kr.")
            return False
        self.saldo -= beløp
        return True

class Sparekonto(Konto):
    def __init__(self, innskudd):
        super().__init__(innskudd)
        self.maks_uttak = 4
        self.antall_uttak = 0

    def uttak(self, beløp:float)->bool:
        if self.maks_uttak == self.antall_uttak:
            return False
        if super().uttak(beløp):
            self.antall_uttak += 1
            return True
        return False
