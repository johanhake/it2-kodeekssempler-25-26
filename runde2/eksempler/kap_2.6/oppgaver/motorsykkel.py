class Motorsykkel:
    def __init__(self, merke, regnr):
        self.merke = merke
        self.regnr = regnr
        self.total_km = 0

    def kjor(self, km):
        self.total_km += km

    def hent_kilometerstand(self):
        return self.total_km

    def skriv_ut(self):
        print(f"Motorsykkel: {self.merke}, {self.regnr}, kmstand: {self.total_km}")
    