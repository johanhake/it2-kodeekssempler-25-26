""" PacTroll"""
import pygame as pg
from pygame.locals import *
from random import randint

pg.init()

BREDDE, HØYDE = 800, 600
BOKS_DIM = 25
INFO_HØYDE = 50
FPS = 24
font = pg.font.SysFont("arial black", 20)


class Boks(pg.sprite.Sprite):
    """
    Grunnklasse for alle bokser i spillet (troll, mat, hindringer).
    Representerer en farget boks med en sort bokstav i midten.
    
    Hvis x og y verdier ikke er gitt trekkes en tilfeldig koordinat
    """

    def __init__(self, app, farge, bokstav, x=-1, y=-1):
        super().__init__()
        self.image = pg.Surface((BOKS_DIM, BOKS_DIM))
        self.rect = self.image.get_rect()
        self.image.fill(farge)
        letter_image = font.render(bokstav, True, "black")
        self.image.blit(letter_image, (5, -2))
        
        # Hvis x og y er gitt plasseres ikke Boksen på et tilfeldig sted
        if x > 0 and y > 0:
            self.rect.x = x 
            self.rect.y = y
        else:
            self.rect.x = randint(0, BREDDE-BOKS_DIM)
            self.rect.y = randint(0, HØYDE-BOKS_DIM)
        
            # Sjekker om tilfeldig plassering kolliderer med eksisterende sprites
            while pg.sprite.spritecollide(self, app.all_sprites, False):
                self.rect.x = randint(0, BREDDE-BOKS_DIM)
                self.rect.y = randint(0, HØYDE-BOKS_DIM)
            
        self.app = app
        self.app.all_sprites.add(self)

class Troll(Boks):
    def __init__(self, app):
        super().__init__(
            app, "green", "T", (BREDDE - BOKS_DIM) // 2, (HØYDE - INFO_HØYDE - BOKS_DIM) // 2
        )
        # Hastighet til Trollet
        self.hastighet = 3
        
        # Attributt som holder på et hinder som akkurat har
        # blitt endret fra mat - hinder etter at Trollet har 
        # spist maten. Dette for å hindre at hinderet blir 
        # plassert for tidlig i gruppen hindre. 
        self.ikke_aktiverte_hinder = []

    def update(self):
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.hastighet
        if keys[K_RIGHT]:
            self.rect.x += self.hastighet
        if keys[K_UP]:
            self.rect.y -= self.hastighet
        if keys[K_DOWN]:
            self.rect.y += self.hastighet
           
        # Sjekker om vi skal aktiverer Hinderet
        if self.ikke_aktiverte_hinder:
    
            # Hvis vi har et hinder har vi akkurat spist en mat. 
            # Hvis vi IKKE kolliderer med dette hindret har vi 
            # gått forbi det og vi kan legge inn det i hindre 
            # gruppen. Går igjennom en kopi av listen slik at vi
            # kan fjerne hindrene fra listen inne i for-lopen
            for h in self.ikke_aktiverte_hinder[:]:
                if not pg.sprite.collide_rect(self, h):
                    self.app.hindre.add(h)
                    self.ikke_aktiverte_hinder.remove(h)
            
        # Sjekket om vi kolliderer med et hinder
        if pg.sprite.spritecollide(self, self.app.hindre, False):
            self.app.game_over = True
        
        # Spiser mat?
        mat_kollisjon = pg.sprite.spritecollide(self, self.app.matbiter, True)
        
        for mat in mat_kollisjon:
            self.app.poeng += 1
            
            # Legger til nytt Hinder i listen med ikke aktiverte 
            # hindre
            self.ikke_aktiverte_hinder.append(Hinder(self.app, mat.rect.x, mat.rect.y))
            
            # Lager en ny Mat
            Mat(self.app)
            
            # Øker hastigheten
            self.hastighet += 1

class Mat(Boks):
    def __init__(self, app):
        super().__init__(app, "yellow", "M")
        self.app.matbiter.add(self)

class Hinder(Boks):
    def __init__(self, app, x=-1, y=-1):
        super().__init__(app, "gray", "H", x=x, y=y)

class App:
    def __init__(self):
        
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((BREDDE, HØYDE))
        pg.display.set_caption("PacTroll")
        self.running = True
        self.game_over = False
        self.poeng = 0
        
        self.stor_font = pg.font.SysFont(None, 70)
        self.liten_font = pg.font.SysFont(None, 30)

        self.hindre = pg.sprite.Group()
        self.matbiter = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self.troll = Troll(self)
        for _ in range(3):
            Mat(self)
            
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        if not self.game_over:
            self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        poeng_tekst = self.liten_font.render(f"{self.poeng:2} poeng", True, "white")
        self.screen.blit(poeng_tekst, (20, 20))
        if self.game_over:
            game_over_tekst = self.stor_font.render("Game Over!", True, "yellow")
            tekst_rect = game_over_tekst.get_rect()
            self.screen.blit(game_over_tekst, ((BREDDE-tekst_rect.width)//2, (HØYDE-tekst_rect.height)//2))
            
        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()


if __name__ == "__main__":
    game = App()
    game.run()