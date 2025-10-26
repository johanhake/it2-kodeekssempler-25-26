class Person:
    def __init__(self, navn, bosted):
        self.navn = navn
        self.bosted = bosted

    def hils(self):
        print(f"Hei, jeg er {self.navn} og jeg kommer fra {self.bosted}.")

    def flytte(self, nytt_bosted):
        if nytt_bosted in ["Bergen", "Stavanger", "Oslo", "Kristiansand"]:
            print(f"{self.navn} flytter fra {self.bosted} til {nytt_bosted}")
            self.bosted = nytt_bosted
        else:
            raise ValueError(f"{nytt_bosted} er ikke med i gyldige steder å flytte til")