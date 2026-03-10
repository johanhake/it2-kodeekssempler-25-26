import pygame as pg
from pygame.locals import *
import math as m
from random import randint, choice
WIDTH, HEIGHT = 700, 700
FPS = 25
RADIUS = 20
LINJEBREDDE = 2
FARTER = [-3, -2, -1, 1, 2, 3]

pg.init()


class Ball(pg.sprite.Sprite):
    def __init__(self, app):
        super().__init__()
        
        # Tilfeldig posisjon på nye baller
        x, y, vx, vy = randint(10,WIDTH-10), randint(10, HEIGHT-10), choice(FARTER), choice(FARTER)
        
        # Lager en surface for bilden til ballen og gjør bakgrunnen transparent (SRCALPHA)
        self.image = pg.Surface((2*RADIUS, 2*RADIUS), SRCALPHA)
        pg.draw.circle(self.image, "yellow", (RADIUS, RADIUS), RADIUS)
        pg.draw.circle(self.image, "red", (RADIUS, RADIUS), RADIUS, LINJEBREDDE)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x-RADIUS, y-RADIUS
        self.app = app
        
        self.vx = vx
        self.vy = vy
        self.collided = False
        
        # Hvis det er overlapp mellom sprites gjenta nye koordinater
        while pg.sprite.spritecollide(self, self.app.all_sprites, False):
            self.rect.x, self.rect.y = randint(10,WIDTH-10), randint(10, HEIGHT-10)

        self.app.all_sprites.add(self)
        
    def collide(self, ball):
        
        if self.collided:
            return 
        
        avst = m.sqrt((self.rect.centerx-ball.rect.centerx)**2+(self.rect.y-ball.rect.y)**2)
        nx, ny = (self.rect.centerx-ball.rect.centerx)/avst, (self.rect.y-ball.rect.y)/avst
        vrel_x, vrel_y = self.vx-ball.vx, self.vy-ball.vy
        vrel_norm = vrel_x*nx + vrel_y*ny

                
        if vrel_norm > 0:
            return

        self.vx -= vrel_norm*nx
        self.vy -= vrel_norm*ny

        ball.vx += vrel_norm*nx
        ball.vy += vrel_norm*ny
        
        self.move()
        ball.move()
        
        self.collided = True
        ball.collided = True

    def move(self):
        if self.collided:
            return
        
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Reflekterer farten hvis møter en av kantene i x-retning
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.vx *= -1
            self.rect.x = min(max(self.rect.x, 0), WIDTH - self.rect.width)
            
            
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vy *= -1
            self.rect.y = min(max(self.rect.y, 0), HEIGHT - self.rect.height)
        
    def update(self):
        
        self.move()
            
        for ball in pg.sprite.spritecollide(self, self.app.all_sprites, False, pg.sprite.collide_mask):
            if self is not ball and not self.collided:
                self.collide(ball)
                    
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
            Ball(self)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    Ball(self)

    def update(self):
        self.frame += 1
        self.all_sprites.update()
        for ball in self.all_sprites:
            ball.collided = False

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
