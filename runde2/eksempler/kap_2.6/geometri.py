import math as m

class Geometri2D:
    """Klasse for 2D objekter """
    def __init__(self, areal:float, omkrets:float)->None:
        self.areal = areal
        self.omkrets = omkrets
        self.navn = "Geomtri2D"

    def __str__(self)->str:
        "Returnerer en tekst representasjon av objektet"
        return f"{self.navn} med areal {self.areal:.2f} og omkrets {self.omkrets:.2f}."

class Kvadrat(Geometri2D):
    """Klasse for Kvadrat"""
    def __init__(self, side:float)->None:
        super().__init__(side*side, 4*side)
        self.side = side
        self.navn = "Kvadrat"
        
    def __add__(self, k2):
        if isinstance(k2, Kvadrat):
            if self.side == k2.side:
                return Rektangel(2*self.side, self.side)
        raise ValueError("Kan bare addere kvadrater med samme sidelengde.")

class Rektangel(Geometri2D):
    """Klasse for Rektangel"""
    def __init__(self, lengde:float, bredde:float)->None:
        super().__init__(lengde*bredde, 2*lengde+2*bredde)
        self.bredde = bredde
        self.lengde = lengde
        self.navn = "Rektangel"


class Sirkel(Geometri2D):
    """Klasse for Sirkel"""
    def __init__(self, radius:float)->None:
        super().__init__(radius*radius*m.pi, 2*radius*m.pi)
        self.radius = radius
        self.navn = "Sirkel"
