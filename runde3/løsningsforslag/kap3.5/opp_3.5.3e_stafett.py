from random import shuffle, uniform


class Klubb:
    def __init__(self, navn: str):
        self.navn = navn
        print(f'Ny klubb: {navn}')
        self.medlemmer = [Medlem('Arild', jente=False)]
        self.medlemmer.append(Medlem('Beate', jente=True))
        self.medlemmer.append(Medlem('Cato', jente=False))
        self.medlemmer.append(Medlem('Dina', jente=True))
        self.medlemmer.append(Medlem('Edward', jente=False))
        self.medlemmer.append(Medlem('Frida', jente=True))
        self.medlemmer.append(Medlem('Gustav', jente=False))
        self.medlemmer.append(Medlem('Hanne', jente=True))
        self.medlemmer.append(Medlem('Ingar', jente=False))
        self.medlemmer.append(Medlem('Jorunn', jente=True))
        self.stafett = None

    def opprett_stafett(self):
        shuffle(self.medlemmer)
        self.stafett = Stafett(self.medlemmer[:8])
        return self.stafett


class Medlem:
    def __init__(self, navn: str, jente=True):
        self.navn = navn
        self.jente = jente


class Stafett:
    def __init__(self, løpere: list):
        print('Ny stafett')
        self.lag = [Lag('Rød', løpere[:4])]
        self.lag.append(Lag('Blå', løpere[4:8]))

    def start(self):
        for lag in self.lag:
            lag.registrer_etappetider()

    def vis_etappetider(self):
        print('\nEtappetider:')
        for lag in self.lag:
            print(f'************* Lag {lag.navn}')
            lag.vis_etappetider()

    def vis_resultatliste(self):
        print('\nResultatliste')
        sortert_liste = sorted(self.lag, key=lambda lag: lag.oppgi_sluttid())
        for i, lag in enumerate(sortert_liste):
            print(f"{i+1}.{lag.navn:6}{lag.oppgi_sluttid():.2f}")


class Lag:
    def __init__(self, navn: str, løpere: list):
        self.navn = navn
        self.løpere = løpere
        self.etappetider = [0.0 for _ in løpere]

    def registrer_etappetider(self):
        self.etappetider = [uniform(11.5, 13.5)
                            if løper.jente else uniform(11.0, 13.0)
                            for løper in self.løpere]

    def vis_etappetider(self):
        [print(f"{løper.navn:8}{tid:.2f}")
            for løper, tid in zip(self.løpere, self.etappetider)]

    def oppgi_sluttid(self) -> float:
        return sum(self.etappetider)


klubb = Klubb('Rask')
klubb.opprett_stafett()
klubb.stafett.start()
klubb.stafett.vis_etappetider()
klubb.stafett.vis_resultatliste()

# Smidig IT-2 © TIP AS 2024