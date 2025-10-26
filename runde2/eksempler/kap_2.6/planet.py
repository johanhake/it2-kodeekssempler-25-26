import math as m

class Planet:
    def __init__(self, navn, solavstand, radius, antall_ringer=0):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antall_ringer = antall_ringer

    def vis_info(self):
        print(f"Planeten {self.navn} er {self.solavstand} M km fra solen og har {self.antall_ringer} ringer")
        
if __name__ == "__main__":
    mars = Planet("Mars", 227.9, 3389.5)
    jupiter = Planet("Jupiter", 778.5, 69911, 4)
    mars.vis_info()
    jupiter.vis_info()

