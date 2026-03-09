# Multipong Del 2 Kollisjoner med padden
import pygame as pg
from pygame.locals import *
from random import choice, randint

WIDTH, HEIGHT = 300, 500
FPS = 24


class Padde(pg.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        self.width = 80
        self.height = 15
        self.image = pg.Surface((self.width, self.height))
        self.image.fill("lightblue")
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 15
        self.rect.centerx = WIDTH / 2
        self.speed = 5
        self.app = app
        self.app.all_sprites.add(self)


class Ball(pg.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.image.fill(choice(["red", "green", "blue"]))
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = randint(0, WIDTH - self.rect.width)
        self.speed = [choice([-1, 1]) * randint(3, 5), randint(3, 5)]
        self.app = app
        self.app.all_sprites.add(self)
        self.app.baller.add(self)

    def update(self):
        # Bruker move_ip til å endre verdien til både x og y
        self.rect.move_ip(self.speed)

        # Snu x-hastigheten hvis den treffer en sidevegg
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] *= -1
            
            # flytt ballen til siden for å unngå umiddelbar ny kollisjon
            self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)

        # Slett ballen når den er utenfor skjermen
        if self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()
            
    def collide(self, hva):
        # Kolliderer vi med en padde
        if isinstance(hva, Padde):
            self.speed[1] *= -1
            # flytt ballen opp for å unngå umiddelbar ny kollisjon
            self.rect.top = hva.rect.top - self.rect.height

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Multipong Del 2")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.baller = pg.sprite.Group()
        self.padde = Padde(self)
        self.frame = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.frame += 1
        # Plasser en ny ball på banen med jevne mellomrom
        if self.frame % FPS == 0:
            Ball(self)

        # Detekter kollisjon  mellom padden og ballene
        hits = pg.sprite.spritecollide(self.padde, self.all_sprites, False)
        for hit in hits:
            pass
            # Sjekk hva som kolliderer og bruk så collide i Ball. 

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