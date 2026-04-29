import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 600, 600
FPS = 60

MIN_WIDTH = 100
MAX_FOOD = 5

pg.init()

class Enhet(pg.sprite.Sprite):
    def __init__(
            self, app, farge: str | tuple[int, int, int],
            x: int , y: int, width: int, height: int,
            bokstav: str = ""
        ):
        super().__init__()
        self.app = app
        self.farge = farge
        self.width = width
        self.height = height
        self.bokstav = bokstav
        
        self.image = pg.Surface((width, height), SRCALPHA)
        self.image.fill(self.farge)
        if self.bokstav:
            self.image.blit(app.font.render(self.bokstav, True, "white"), (5, 5))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        while pg.sprite.spritecollide(self, self.app.sprites, False):
            self.rect.x, self.rect. y = randint(0, WIDTH - 40), randint(-HEIGHT, 0)

        self.app.sprites.add(self)

class Bunndyr(Enhet):
    
    def update(self):
        self.image = pg.Surface((self.width, self.height), SRCALPHA)
        self.image.fill(self.farge)
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        keys = pg.key.get_pressed()

        if   keys[pg.K_d]: self.rect.x += 5
        elif keys[pg.K_a]: self.rect.x -= 5

        if   self.rect.right > WIDTH: self.rect.right = WIDTH
        elif self.rect.left < 0:      self.rect.left = 0

class Plankton(Enhet):
    def __init__(self, app, farge: str, bokstav: str):
        super().__init__(app, farge, randint(0, WIDTH - 40), randint(-HEIGHT, 0), 40, 40, bokstav)
        if self.farge == "green":
            self.app.grønn.add(self)
        else:
            self.app.rød.add(self)

    def update(self):
        self.rect.y += 2

        if self.rect.top > HEIGHT:
            self.kill()

class App:
    def __init__(self):
        pg.display.set_caption("Bunndyr")
        self.clock = pg.time.Clock()
        self.win = pg.display.set_mode((WIDTH, HEIGHT))
        self.font = pg.font.SysFont(None, 50)
        self.running = True
        self.frame = 0
        self.food = 1

        self.sprites = pg.sprite.Group()
        self.grønn = pg.sprite.Group()
        self.rød = pg.sprite.Group()
        self.bunndyr = Bunndyr(self, "grey", WIDTH // 2 - 100, HEIGHT - 50, 200, 50)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.food + 1 <= MAX_FOOD:
                    self.food += 1

    def update(self):
        self.sprites.update()

        if pg.sprite.spritecollide(self.bunndyr, self.grønn, True):
            self.bunndyr.width += 10
            self.bunndyr.rect.x -= 5

        if pg.sprite.spritecollide(self.bunndyr, self.rød, True):
            self.bunndyr.width -= 10
            self.bunndyr.rect.x += 5

        if self.bunndyr.width >= WIDTH or self.bunndyr.width <= MIN_WIDTH:
            self.running = False
        
    def draw(self):
        self.win.fill("black")
        self.sprites.draw(self.win)
        pg.display.flip()

    def step(self):
        self.frame += 1
        if (self.frame / FPS) % 1 == 0:
            Plankton(self, "red", "R")
            for _ in range(self.food):
                Plankton(self, "green", "G")
        self.clock.tick(FPS)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.step()
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()
 