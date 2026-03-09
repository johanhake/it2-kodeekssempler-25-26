import pygame as pg
from pygame.locals import *
from random import randint
WIDTH, HEIGHT = 700, 700
FPS = 25
RADIUS = 20
LINJEBREDDE = 2

pg.init()


class Ball(pg.sprite.Sprite):
    def __init__(self, app, x, y, vx, vy):
        super().__init__()
        
        # Lager en surface for bilden til ballen og gjør bakgrunnen transparent (SRCALPHA)
        self.image = pg.Surface((2*RADIUS, 2*RADIUS), SRCALPHA)
        pg.draw.circle(self.image, "yellow", (RADIUS, RADIUS), RADIUS)
        pg.draw.circle(self.image, "red", (RADIUS, RADIUS), RADIUS, LINJEBREDDE)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x-RADIUS, y-RADIUS
        self.app = app
        self.app.all_sprites.add(self)
        self.vx = vx
        self.vy = vy
        self.frame_start = self.app.frame

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Reflekterer farten hvis møter en av kantene i x-retning
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1
            
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vy *= -1
            
        # Fjerner ballen etter 5 sekunder
        if self.app.frame - self.frame_start > 5*FPS:
            self.kill()
        
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.font = pg.font.SysFont(None, 50)
        self.frame = 0
        
        # Lager spilleobjektene
        for _ in range(5):
            Ball(self, randint(10,WIDTH-10), randint(10, HEIGHT-10), randint(-5,5), randint(-5,5))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
    
            if event.type == pg.MOUSEMOTION:
                if event.buttons[0]:
                    # Lager ny Ball med posisjon til musen og fart basert på relativ fart til mus. 
                    Ball(self, event.pos[0], event.pos[1], event.rel[0], event.rel[1])

    def update(self):
        self.frame += 1
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        tekst = self.font.render(f"{self.frame/FPS:.1f} s", True, "white")
        self.screen.blit(tekst, (20, 20))
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
