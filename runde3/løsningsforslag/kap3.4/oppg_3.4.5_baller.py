import pygame as pg
from pygame.locals import *
from random import randint
WIDTH, HEIGHT = 500, 500
FPS = 24
RADIUS = 10
LINJEBREDDE = 2

pg.init()

class Ball(pg.sprite.Sprite):
    def __init__(self, app, x, y, vx, vy):
        super().__init__()
        self.image = pg.Surface((2*RADIUS, 2*RADIUS))
        pg.draw.circle(self.image, "yellow", (RADIUS, RADIUS), RADIUS)
        pg.draw.circle(self.image, "red", (RADIUS, RADIUS), RADIUS, LINJEBREDDE)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x-RADIUS, y-RADIUS
        self.app = app
        self.app.all_sprites.add(self)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1

        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vy *= -1

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # Lager spilleobjektene
        for _ in range(5):
            Ball(self, randint(10,WIDTH-10), randint(10, HEIGHT-10), randint(-5,5), randint(-5,5))

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
