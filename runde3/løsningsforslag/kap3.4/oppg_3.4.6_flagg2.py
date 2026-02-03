import pygame as pg
from pygame.locals import *
from random import randint
WIDTH, HEIGHT = 500, 500
FPS = 5
RADIUS = 10
LINJEBREDDE = 2

pg.init()

class Sverige(pg.sprite.Sprite):
    def __init__(self, app, bredde):
        super().__init__()
        høyde = bredde*(5/8)
        self.image = pg.Surface((bredde, høyde))
        
        blå = (0, 106, 167)
        gul = (254, 204, 0)
        pg.draw.rect(self.image, blå, (0, 0, bredde, høyde))
        pg.draw.rect(self.image, gul, (0, høyde*2/5, bredde, høyde/5))
        pg.draw.rect(self.image, gul, (5/16*bredde, 0, bredde/8, høyde))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = randint(0,WIDTH-self.rect.width), randint(0, HEIGHT-self.rect.height)
        self.app = app
        self.app.all_sprites.add(self)

    def update(self):
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = randint(0, HEIGHT - self.rect.height)
        
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame Flagg")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # Lager spilleobjektene
        Sverige(self, 100)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
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
    app = App()
    app.run()
