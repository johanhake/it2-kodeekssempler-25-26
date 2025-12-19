from time import sleep

class Tallvisere:
    def __init__(self, verdi, maks_verdi):
        self.verdi = verdi
        self.maks_verdi = maks_verdi
        
    def set_verdi(self, verdi):
        self.verdi = verdi
        
    def øk(self):
        self.verdi += 1
        if self.verdi == self.maks_verdi:
            self.verdi = 0

    def vis_verdi(self):
        return f"{self.verdi:02}"
    
class DigitalKlokke:
    def __init__(self):
        self.timer = Tallvisere(0,24)
        self.minutter = Tallvisere(0, 60)
        
    def vis_tid(self):
        return f"{self.timer.vis_verdi()}:{self.minutter.vis_verdi()}"
        
    def tid_går(self):
        while True:
            print(self.vis_tid())
            self.minutter.øk()
            if self.minutter.verdi == 0:
                self.timer.øk()
            sleep(0.05)
        
klokke = DigitalKlokke()

klokke.tid_går()