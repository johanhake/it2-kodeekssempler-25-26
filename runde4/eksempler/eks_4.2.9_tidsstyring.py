# Eksempel på tidsstyring i Pygame
import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 500, 600
FPS = 24

# Ordbok som mapper farger til x-verdi
FARGER_TIL_X = {
    "red": 75,
    "blue": 160,
    "green": 245,
    "orange": 330,
    "purple": 415    
}

# Egne hendelser
GRØNNBALL = pg.USEREVENT
ORANGEBALL = pg.USEREVENT + 1
PURPLEBALL = pg.USEREVENT + 2


class Ball(pg.sprite.Sprite):
    def __init__(self, app, color):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, color, (10, 10), 10)
        self.rect.x = FARGER_TIL_X[color]
        self.rect.y = 0
        self.app = app
        self.app.all_sprites.add(self)

    def update(self):
        self.rect.y += 5

        # Fjern ballen fra sprite-gruppen når den går utenfor vinduet
        if self.rect.top > HEIGHT:
            self.kill()

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tidsstyrte handlinger")
        self.timer = pg.time.get_ticks()
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # ALTERNATIV 3a (Fast tidsintervall)
        # lag en burkerdefinert hendelse hvert 2. sekund
        #pg.time.set_timer(GRØNNBALL, 2000)
        
        # ALTERNATIV 3b (Fast tidsintervall, men en annen hendelse)
        # lag en annen burkerdefinert hendelse hvert 0.5. sekund
        #pg.time.set_timer(ORANGEBALL, 500)
        
        # ALTERNATIV 4 (Tilfeldig tidsintervall, også en annen hendelse)
        # lag en annen brukerdefinert hendelse ved tilfeldig tispunkt
        # i snitt hvert 1. sekund
        #pg.time.set_timer(PURPLEBALL, randint(500, 1500), loops=1)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == GRØNNBALL:
                Ball(self, "green")
            elif event.type == ORANGEBALL:
                Ball(self, "orange")
            elif event.type == PURPLEBALL:
                Ball(self, "purple")
                pg.time.set_timer(PURPLEBALL, randint(500, 1500), loops=1)

    def update(self):
        # ALTERNATIV 1 (Tilfeldig tidsintervall)
        # legg til en ny rød ball ved tilfeldig tidspunkt
        # i snitt  hvert sekund
        if randint(0, FPS - 1) == 0:
            Ball(self, "red")

        # ALTERNATIV 2 (Fast tidsintervall)
        # legg til en ny blå ball hvert sekund
        # Husk å sette self.timer = pg.time.get_ticks() i __init__
        # if pg.time.get_ticks() - self.timer > 1000:
        #     self.timer = pg.time.get_ticks()
        #     Ball(self, "blue")

        # Kun for å sjekke at ballene fjernes fra minnet
        # når de er utenfor vinduet.
        print(len(self.all_sprites))

        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS, 2024