import pygame as pg
from pygame.locals import *
from random import randint, random
import math as m
import time

WIDTH, HEIGHT = 1000, 750
FPS = 100
W, H = 25, 25
FRI = 50
V = 10
VS = V/2

class SpilleObjekt(pg.sprite.Sprite):
    def __init__(self, app, farge):
        super().__init__()
        self.image = pg.Surface((W, H))
        pg.draw.rect(self.image, farge, (0, 0, W, H))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.nye_koordinater()
        self.app = app

        # Hvis det er overlapp mellom sprites gjenta nye koordinater
        while pg.sprite.spritecollide(self, self.app.all_sprites, False):
            self.rect.x, self.rect.y = self.nye_koordinater()

        # Ingen overlapp, legg til sprite til all_sprites
        self.app.all_sprites.add(self)

    def update(self):
        NotImplemented

    def nye_koordinater(self):
        return (0, 0)

class Menneske(SpilleObjekt):
    def __init__(self, app):
        super().__init__(app, "green")
        self.har_sau = False

    def nye_koordinater(self):
        return (FRI/4, (HEIGHT-H)/2)

    def bytt_sau(self):
        self.har_sau = not self.har_sau
        if self.har_sau:
            pg.draw.rect(self.image, "seagreen", (0, 0, W, H))
        else:
            pg.draw.rect(self.image, "green", (0, 0, W, H))

    def update(self):
        pressed_keys = pg.key.get_pressed()
        vx, vy = 0, 0

        # Finner farten
        v = VS if self.har_sau else V

        # Sjekker tastene asdw (og piltaster) bruker -= og += slik at effekten av å 
        # holde inn både venstre og høyre tast nuller ut hverandre. 
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            vx -= v
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            vx += v
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            vy -= v
        if pressed_keys[K_s] or pressed_keys[K_DOWN]:
            vy += v

        # Flytter mennesket
        self.rect.move_ip(vx, vy)

        # Sjekker for kollisjon med hindringer. 
        for hindring in pg.sprite.spritecollide(self, self.app.hindringer, False):
            # Sjekker om det er en horrisontal eller en vertikal kollissjon 
            # NB! Denne sjekken er rett og slett litt buggy...
            avstand_x = abs(hindring.rect.center[0] - self.rect.center[0])
            avstand_y = abs(hindring.rect.center[1] - self.rect.center[1])
            if avstand_x > avstand_y:
                # Hvis horrisontal sjekke hvilken side vi er på og flytter mennesket tilsvarende
                if vx > 0:
                    self.rect.right = hindring.rect.left
                else:
                    self.rect.left = hindring.rect.right
                    
            if avstand_x < avstand_y:
                # Hvis vertikal sjekke hvilken side vi er på og nullstiller ev fart i y retning
                if vy > 0:
                    self.rect.bottom = hindring.rect.top
                else:
                    self.rect.top = hindring.rect.bottom
                    

        # Sjekker kollisjon med kanter
        self.rect.clamp_ip(0,0,WIDTH, HEIGHT)
        # if self.rect.left + vx < 0 or self.rect.right + vx > WIDTH:
        #     vx = 0
        # if self.rect.top + vy < 0 or self.rect.bottom + vy > HEIGHT:
        #     vy = 0


class Hindring(SpilleObjekt):
    def __init__(self, app):
        super().__init__(app, "blue")
        self.app.hindringer.add(self)

    def nye_koordinater(self):
        return (randint(FRI, WIDTH-FRI-W), randint(0, HEIGHT-H))

class Spøkelse(SpilleObjekt):
    def __init__(self, app):
        super().__init__(app, "red")
        self.app.spøkelser.add(self)
        vinkel = random()*m.pi*2
        self.vx = m.cos(vinkel)*VS
        self.vy = m.sin(vinkel)*VS

    def nye_koordinater(self):
        return (randint(FRI, WIDTH-FRI-W), randint(0, HEIGHT-H))

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Sjekker kollisjon med kanter
        if self.rect.left < FRI or self.rect.right > WIDTH - FRI:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.vy *= -1

class Sau(SpilleObjekt):
    def __init__(self, app):
        super().__init__(app, "white")
        self.app.sauer.add(self)

    def nye_koordinater(self):
        return (randint(WIDTH-FRI, WIDTH-W), randint(0, HEIGHT-H))

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Manic Mansion")
        self.running = True
        self.poeng = 0
        self.font_small = pg.font.SysFont("Verdana", 20)
        self.all_sprites = pg.sprite.Group()
        self.hindringer = pg.sprite.Group()
        self.spøkelser = pg.sprite.Group()
        self.sauer = pg.sprite.Group()

        # Legger til alle spritene
        for _ in range(3):
            Sau(self)
            Hindring(self)

        Spøkelse(self)
        self.menneske = Menneske(self)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

        # Sjekker for kollisjon med sau
        for sau in self.sauer:

            if pg.sprite.collide_rect(self.menneske, sau):
                # Hvis vi allerede har en sau dør vi
                if self.menneske.har_sau:
                    self.død()

                self.menneske.bytt_sau()
                sau.kill()

        # Sjekker for avlevering av sau
        if self.menneske.har_sau and self.menneske.rect.right < FRI:
            self.menneske.bytt_sau()
            self.poeng += 1

            # Øker antallet hinder og legger til Sau
            Sau(self)
            Hindring(self)
            Spøkelse(self)

        # Sjekker om vi dør!
        if pg.sprite.spritecollide(self.menneske, self.spøkelser, False):
            self.død()

    def død(self):
        self.screen.fill("red")
        pg.display.update()
        time.sleep(4)
        self.running = False

    def draw(self):
        if not self.running:
            return
        self.screen.fill("black")
        pg.draw.rect(self.screen, "darkgreen",(0,0,FRI,HEIGHT))
        pg.draw.rect(self.screen, "darkgreen",(WIDTH-FRI,0,FRI,HEIGHT))
        self.all_sprites.draw(self.screen)
        poeng = self.font_small.render(str(self.poeng), True, "white")
        self.screen.blit(poeng, (10,10))
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
