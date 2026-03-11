""" PacTroll"""
import pygame as pg
from pygame.locals import *
from random import randint

pg.init()

BREDDE, HØYDE = 800, 600
BOKS_DIM = 25
INFO_HØYDE = 50
FPS = 24
font = pg.font.SysFont("arial black", 20)


class Boks(pg.sprite.Sprite):
    """
    Grunnklasse for alle bokser i spillet (troll, mat, hindringer).
    Representerer en farget boks med en sort bokstav i midten.
    
    Hvis x og y verdier ikke er gitt trekkes en tilfeldig koordinat
    """

    def __init__(self, app, farge, bokstav, x=-1, y=-1):
        super().__init__()
        self.image = pg.Surface((BOKS_DIM, BOKS_DIM))
        self.rect = self.image.get_rect()
        self.image.fill(farge)
        letter_image = font.render(bokstav, True, "black")
        self.image.blit(letter_image, (5, -2))
        
        self.rect.x = x if x > 0 else randint(0, BREDDE-BOKS_DIM)
        self.rect.y = y if y > 0 else randint(0, HØYDE-BOKS_DIM)
        
        # Sjekker om tilfeldig plassering kolliderer med eksisterende sprites
        while pg.sprite.spritecollide(self, app.all_sprites, False):
            self.rect.x = x if x > 0 else randint(0, BREDDE-BOKS_DIM)
            self.rect.y = y if y > 0 else randint(0, HØYDE-BOKS_DIM)
            
        self.app = app
        self.app.all_sprites.add(self)


class Troll(Boks):
    def __init__(self, app):
        super().__init__(
            app, "green", "T", (BREDDE - BOKS_DIM) // 2, (HØYDE - INFO_HØYDE - BOKS_DIM) // 2
        )
        self.hastighet = 3

    def update(self):
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.hastighet
        if keys[K_RIGHT]:
            self.rect.x += self.hastighet
        if keys[K_UP]:
            self.rect.y -= self.hastighet
        if keys[K_DOWN]:
            self.rect.y += self.hastighet

class Mat(Boks):
    def __init__(self, app):
        super().__init__(app, "yellow", "M")
        self.app.matbiter.add(self)

class Hinder(Boks):
    def __init__(self, app):
        super().__init__(app, "gray", "H", x, y)
        self.app.hindre.add(self)

class App:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((BREDDE, HØYDE))
        pg.display.set_caption("PacTroll")
        self.running = True
        self.game_over = False
        self.poeng = 0

        self.hindre = pg.sprite.Group()
        self.matbiter = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.troll = Troll(self)
        for _ in range(3):
            Mat(self)
            
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
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
    game = App()
    game.run()