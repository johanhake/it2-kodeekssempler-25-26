import pygame as pg
from pygame.locals import *
from random import randint
BREDDE, HØYDE = 1200, 700
FPS = 25

pg.init()

# Colors
#MØRKEGRÅ = (100, 100, 100)
GRÅ = (150, 150, 150)
LYSEGRÅ = (200, 200, 200)
SORT = (0, 0, 0)

NÆR = 0
BORTE = 1
#LANGT_BORTE = 2

class Stjerne(pg.sprite.Sprite):
    def __init__(self, app, type):
        super().__init__()
        if type == NÆR:
            radius = 3
            farge = LYSEGRÅ
            self.vx = -randint(10, 15)
        else:
            radius = 2
            farge = GRÅ
            self.vx = -randint(2, 5)

        self.image = pg.Surface((radius*2, radius*2), SRCALPHA)
        
        pg.draw.circle(self.image, farge, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(radius, BREDDE-radius), randint(radius, HØYDE-radius))
        
        self.app = app
        self.app.all_sprites.add(self)
        
    def update(self):
        self.rect.x += self.vx
        if self.rect.right < 0:
            if self.app.knapp_trykket:
                self.kill()
            else:
                self.rect.left = BREDDE
    
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((BREDDE, HØYDE))
        pg.display.set_caption("Stjerner!")
        self.running = True
        self.knapp_trykket = False
        self.all_sprites = pg.sprite.Group()
        
        # Lager spilleobjektene
        for antall, type in [(200, BORTE), (100, NÆR)]:
            for _ in range(antall):
                Stjerne(self, type)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
    
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.knapp_trykket = True
                    print("Fjerner!")
            
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.knapp_trykket = False
                    print("Beholder!")

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
