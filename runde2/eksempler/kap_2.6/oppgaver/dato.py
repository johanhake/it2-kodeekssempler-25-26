class Dato:
    dager_maaneder = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    maaneder_txt = maaneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", 
            "Juli", "August", "September", "Oktober", "November", "Desember"]
    def __init__(self, ny_dag, ny_maaned, nytt_aar):
        self.dag = ny_dag
        self.maaned = ny_maaned
        self.aar = nytt_aar

    def self_dager_i_maanader(self):
        if self.maaned == 2 and self.aar % 4 == 0 and self.aar % 400 != 0:
            return 29
        return Dato.dager_maaneder[self.maaned-1]

    def hent_aar(self):
        return self.aar

    def __str__(self):
        return f"{self.dag:02}.{self.maaned:02}.{self.aar}"

    def er_dag(self, dag):
        return self.dag == dag

    def oek_maaned(self, maaned):
        self.maaned += maaned
        while self.maaned > 12:
            self.maaned -= 12
            self.aar += 1

    def oek(self,dag):
        self.dag += dag
        while self.dag > self.self_dager_i_maanader():
            self.dag -= self.self_dager_i_maanader()
            self.oek_maaned(1)

if __name__ == "__main__":
    d = Dato(15, 12, 23)

    d.oek(15)
    print(d)
    d.oek(3)
    print(d)
    d.oek(58)
    print(d)
