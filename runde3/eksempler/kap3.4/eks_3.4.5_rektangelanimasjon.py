import pygame as pg
from pygame.locals import *
WIDTH, HEIGHT = 500, 500
FPS = 24

pg.init()

class Rektangel(pg.sprite.Sprite):
    def __init__(self, app, x, y, w, h, farge):
        super().__init__()
        self.image = pg.Surface((w, h))
        pg.draw.rect(self.image, farge, (0, 0, w, h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.app = app
        self.app.all_sprites.add(self)

    def update(self):
        # Endre på self.rect her og ev. self.image
        self.rect.x += 5
        self.rect.y += 5
        
class Oppover(Rektangel):
    
    def update(self):
        # Endre på self.rect her og ev. self.image
        self.rect.x += 5
        self.rect.y -= 5
           
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # Lager de ulike Spritene
        Rektangel(self, 12, 8, 200, 10, "orange")
        Oppover(self, 62, 600, 50, 50, "blue")

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
