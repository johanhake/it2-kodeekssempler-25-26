global_lånerID = 0

class Bok:
    def __init__(self, tittel:str, forfatter:str)->None:
        self.tittel = tittel
        self.forfatter = forfatter
        self.utlånt = None
        
    def vis_info(self):
        
        if self.utlånt is None:
            print(f"Boken {self.tittel} er skreven av {self.forfatter} og er ikke utlånt")
        else:
            print(f"Boken {self.tittel} er skreven av {self.forfatter} og er utlånt til låner med ID {self.utlånt.lånerID}")
            
class Låner:
    def __init__(self)->None:
        global global_lånerID
        global_lånerID += 1
        self.lånerID = global_lånerID 
        self.lånte_bøker = []
        
    def lån_bok(self, bok:Bok)->None:
        if bok.utlånt is None:
            self.lånte_bøker.append(bok)
            bok.utlånt = self
            print(f"Boken {bok.tittel} er nå utlånt til låner med ID: {self.lånerID}.")
        else:
            print(f"Boken er allerede utlånt til låner med ID: {bok.utlånt.lånerID}")
            
    def lever_tilbake_bok(self, bok:Bok)->None:
        if bok.utlånt is None:
            print(f"Boken {bok.tittel} kan ikke leveres tilbake ettersom den ikke er utlånt.")
        elif bok.utlånt is not self:
            print(f"Boken {bok.tittel} kan ikke leveres tilbake ettersom den er lånt av en annen låner.")
        else:
            self.lånte_bøker.remove(bok)
            bok.utlånt = None
            print(f"Boken {bok.tittel} er nå levert tilbake")