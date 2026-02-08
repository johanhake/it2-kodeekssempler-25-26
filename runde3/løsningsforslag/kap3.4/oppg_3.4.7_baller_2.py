import pygame as pg
from pygame.locals import *
from random import randint
WIDTH, HEIGHT = 1200, 700
FPS = 24
RADIUS = 20
LINJEBREDDE = 2
KANTBREDDE = 20

pg.init()

antall_baller = 0

class Ball(pg.sprite.Sprite):
    def __init__(self, app, x, y, vx, vy):
        super().__init__()
        global antall_baller
        
        if antall_baller < 20:
            farge = "red"
        elif antall_baller < 40:
            farge = "green"
        elif antall_baller < 60:
            farge = "blue"
        else:
            farge = "black"
        # Lager en surface for bilden til ballen og gjør bakgrunnen transparent (SRCALPHA)
        self.image = pg.Surface((2*RADIUS, 2*RADIUS), SRCALPHA)
        pg.draw.circle(self.image, farge, (RADIUS, RADIUS), RADIUS)
        pg.draw.circle(self.image, "yellow", (RADIUS, RADIUS), RADIUS, LINJEBREDDE)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x-RADIUS, y-RADIUS
        self.app = app
        self.app.all_sprites.add(self)
        self.vx = vx
        self.vy = vy
        antall_baller += 1

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Forsvinner og kommer tilbake!
        if self.rect.right > WIDTH-KANTBREDDE:
            self.rect.left = KANTBREDDE
            
        if self.rect.left < KANTBREDDE:
            self.rect.right = WIDTH-KANTBREDDE

        # Spretter fra topp og bunn
        if self.rect.top < KANTBREDDE:
            self.vy *= -1
        
        if self.rect.bottom > HEIGHT - KANTBREDDE and \
            (self.rect.right < WIDTH/3 or \
                self.rect.left > WIDTH*2/3):
            self.vy *= -1
            
        # Kommer ut av bilden
        if self.rect.top > HEIGHT:
            self.kill()

class Kant(pg.sprite.Sprite):
    def  __init__(self, app):
        super().__init__()
        # Lager en surface som er like stor som hele bildet
        self.image = pg.Surface((WIDTH, HEIGHT), SRCALPHA)
        
        # Venstre og høyre kanter
        pg.draw.rect(self.image, "blue", (0, 0, KANTBREDDE, HEIGHT))
        pg.draw.rect(self.image, "blue", (WIDTH-KANTBREDDE, 0, KANTBREDDE, HEIGHT))
        
        # Topp
        pg.draw.rect(self.image, "red", (KANTBREDDE, 0, WIDTH-2*KANTBREDDE, KANTBREDDE))
        
        # Bunn
        pg.draw.rect(self.image, "red", (KANTBREDDE, HEIGHT - KANTBREDDE, WIDTH/3-KANTBREDDE, KANTBREDDE))
        pg.draw.rect(self.image, "red", (WIDTH*2/3, HEIGHT - KANTBREDDE, WIDTH/3-KANTBREDDE, KANTBREDDE))
        
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

        self.app = app
        self.app.all_sprites.add(self)


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # Lager spilleobjektene
        Kant(self)
        for _ in range(5):
            Ball(self, randint(10,WIDTH-10), randint(10, HEIGHT-10), randint(-5,5), randint(-5,5))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
    
            if event.type == pg.MOUSEMOTION:
                if event.buttons[0]:
                    # Lager ny Ball med posisjon til musen og fart basert på relativ fart til mus.
                    x = min(max(event.pos[0], KANTBREDDE+RADIUS), WIDTH-(KANTBREDDE+RADIUS))
                    y = min(max(event.pos[1], KANTBREDDE+RADIUS), HEIGHT-(KANTBREDDE+RADIUS))
                    Ball(self, x, y, event.rel[0], event.rel[1])

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
