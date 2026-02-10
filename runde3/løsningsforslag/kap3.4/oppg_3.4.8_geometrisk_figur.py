import pygame as pg
from pygame.locals import *
from random import randint
WIDTH, HEIGHT = 1200, 700
FPS = 24
RADIUS = 20
LINJEBREDDE = 2
KANTBREDDE = 20

pg.init()

# Colors
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (220, 60, 60)
BLUE = (80, 50, 255)
YELLOW = (255, 200, 50)
BLACK = (0, 0, 0)
class Rakett(pg.sprite.Sprite):
    antall = 0
    def __init__(self, app, x, y, height, vx, vy):
        super().__init__()
        Rakett.antall += 1

        # Lager en surface for bilden til ballen og gjør bakgrunnen transparent (SRCALPHA)

        self.image = self.draw(height)
        self.rect = self.image.get_rect()
        
        self.rect.x = x-self.rect.width/2
        self.rect.y = y-self.rect.height/2
        self.app = app
        self.app.all_sprites.add(self)
        self.vx = vx
        self.vy = vy
        
    def draw(self, height):
        # --- Geometriske proporsjoner ---
        nose_h = height * 0.15
        body_h = height * 0.65
        fin_h  = height * 0.20
        flame_h = height * 0.20

        body_w = height * 0.25
        fin_w = height * 0.18
        window_r = height * 0.05
        
        # Bredde til tegningen
        width = 2*fin_w + body_w

        # Tegnebrette til raketten
        image = pg.Surface((width, height), SRCALPHA)

        # Øverste punkt (nesespiss)
        top_y = 0
        
        # Midt i raketten
        cx = width / 2

        # --- Nese (trekant) ---
        nose_points = [
            (cx, top_y),                             # toppspiss
            (cx - body_w / 2, top_y + nose_h),
            (cx + body_w / 2, top_y + nose_h)
        ]
        pg.draw.polygon(image, RED, nose_points)

        # --- Kropp (rektangel) ---
        body_rect = pg.Rect(
            cx - body_w / 2,
            top_y + nose_h,
            body_w,
            body_h
        )
        pg.draw.rect(image, GREY, body_rect)

        # --- Vindu (sirkel) ---
        pg.draw.circle(
            image,
            BLUE,
            (cx, int(top_y + nose_h + body_h * 0.35)),
            int(window_r)
        )
        pg.draw.circle(
            image,
            WHITE,
            (cx, int(top_y + nose_h + body_h * 0.35)),
            int(window_r * 0.8)
        )

        # --- Flamme (polygon) ---
        flame_top = top_y + nose_h + body_h
        flame_points = [
            (cx - body_w * 0.25, flame_top),
            (cx + body_w * 0.25, flame_top),
            (cx + body_w * 0.15, flame_top + flame_h * 0.5),
            (cx,            flame_top + flame_h),
            (cx - body_w * 0.15, flame_top + flame_h * 0.5),
        ]
        pg.draw.polygon(image, YELLOW, flame_points)

        # --- Finner (trekanter) ---
        fin_top_y = flame_top - fin_h 

        left_fin = [
            (cx - body_w / 2, fin_top_y),
            (cx - body_w / 2 - fin_w, fin_top_y + fin_h),
            (cx - body_w / 2, fin_top_y + fin_h),
        ]
        right_fin = [
            (cx + body_w / 2, fin_top_y),
            (cx + body_w / 2 + fin_w, fin_top_y + fin_h),
            (cx + body_w / 2, fin_top_y + fin_h),
        ]
        pg.draw.polygon(image, RED, left_fin)
        pg.draw.polygon(image, RED, right_fin)
        
        return image
            
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or \
            self.rect.left < 0 or self.rect.right > WIDTH:
                self.drep()
                
    def drep(self):
        Rakett.antall -= 1
        self.kill()
        
class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("PyGame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        
        # Lager spilleobjektene
        #Rakett(self, )

    def handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
    
            if event.type == pg.MOUSEMOTION:
                if event.buttons[0]:
                    # Lager ny Rakett med posisjon til musen og fart basert på relativ fart til mus.
                    x = min(max(event.pos[0], KANTBREDDE+RADIUS), WIDTH-(KANTBREDDE+RADIUS))
                    y = min(max(event.pos[1], KANTBREDDE+RADIUS), HEIGHT-(KANTBREDDE+RADIUS))
                    Rakett(self, x, y, randint(50, 250), event.rel[0], event.rel[1])

    def update(self):
        self.all_sprites.update()
        print("Antall raketter:", Rakett.antall)

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
