import pygame as pg
from pygame.locals import *
from random import choice, randint, random, uniform
import math as m
import time

FARGER = ["red", "green"]*2 +["brown"]
WIDTH, HEIGHT = 600, 800
FPS = 24
pg.init()
ANTALL_EPLER = 15

# De ulike fontene som skal brukes
font = pg.font.SysFont("Verdana", 60)
font_medium = pg.font.SysFont("Verdana", 35)
game_over = font.render("Game Over", True, "white")
start_game = font_medium.render("'S' - start game", True, "black")

W = 50
H = 50
VB = 15

class SpillObjekt(pg.sprite.Sprite):
    def __init__(self, app, w, h, farge, x, y):
        super().__init__()
        self.image = pg.Surface((w, h))
        pg.draw.rect(self.image, farge, (0, 0, w, h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.app = app
        self.farge = farge

        # Ingen overlapp, legg til sprite til all_sprites
        self.app.all_sprites.add(self)
        
    def update(self):
        NotImplemented
    
class Eple(SpillObjekt):
    def __init__(self, app):
        super().__init__(app, W, H, choice(FARGER), randint(0, WIDTH-W), H/2)
        self.app.epler.add(self)

        self.vx = 0
        self.vy = uniform(0.8, 1.2)*VB
        self.boom = False
        self.app.epler_igjen -= 1

    def update(self):
        # Endrer posisjon til rect
        self.rect.move_ip(self.vx, self.vy)

        # Hvis eplet faller utenfor skjermen
        if self.rect.top > HEIGHT:
            self.kill()
            self.app.nytt_eple()

        # Hvis fanges av kurv sjekk farge og fjern eple
        if self.rect.colliderect(self.app.kurv.rect) and not self.boom:
            
            if self.app.kurv.farge == self.farge:
                self.app.poeng += 1
            else:
                self.app.poeng -= 1

            self.kill()
            self.app.nytt_eple()

        # Har eplet passert kurven ved siden. Da registreres den som en boom
        elif self.rect.bottom > self.app.kurv.rect.top:
            self.boom = True


class Kurv(SpillObjekt):
    def __init__(self, app):
        super().__init__(app, 3*W, H, "red", (WIDTH+W)/2, HEIGHT - 2.5*H)

    def update(self):
        pressed_keys = pg.key.get_pressed()
        
        dx = 0
        # Sjekker tastene as (og piltaster)
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            dx =  -2*VB

        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            dx = 2*VB

        if pressed_keys[K_r]:
            self.farge = "red"
            pg.draw.rect(self.image, self.farge, (0,0,self.rect.w,self.rect.h))

        if pressed_keys[K_g]:
            self.farge = "green"
            pg.draw.rect(self.image, self.farge, (0,0,self.rect.w,self.rect.h))
    
        self.rect.move_ip(dx, 0)

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class App:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Eplesanking")
        self.all_sprites = pg.sprite.Group()
        self.epler = pg.sprite.Group()
        self.paused = True
        self.running = True
        self.slutt = True
        self.kurv = Kurv(self)
        self.epler_igjen = ANTALL_EPLER

    def nytt_eple(self):
        if self.epler_igjen > 0:
            Eple(self)
        else:
            self.slutt = True

    def start(self):
        
        # Fjerner alle epler fra de ulike gruppene
        for eple in self.epler:
            eple.kill()
        
        # Starter med et eple
        Eple(self)
    
        # Nullstiller poengen og antall baller tapt
        self.poeng = 0
        self.slutt = False

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if  event.key == K_s and self.paused:
                    self.paused = False
                    self.start()

    def update(self):
        self.all_sprites.update()

    def draw(self):
        if self.paused:
            self.screen.fill("green")
            self.screen.blit(start_game, (30,250))
            
        elif self.slutt:
            time.sleep(1)
            
            self.screen.fill("red")
            poeng = font_medium.render(f"Poeng: {self.poeng}" , True, "white")
            self.screen.blit(poeng, (30, 250 + game_over.get_rect().height+5))
            self.screen.blit(game_over, (30,250))
            self.paused = True
            pg.display.update()
            time.sleep(5)

        else:
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            poeng = font_medium.render(f"{self.poeng} ({self.epler_igjen})", True, "white")
            self.screen.blit(poeng, (10, HEIGHT-1.5*H))
        
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
