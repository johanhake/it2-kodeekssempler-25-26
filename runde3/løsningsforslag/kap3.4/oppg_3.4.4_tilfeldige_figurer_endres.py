import pygame as pg
from random import randint, choice

# Initialiserer/starter pygame
pg.init()

BREDDE = 500
HOYDE  = 500
vindu = pg.display.set_mode([BREDDE, HOYDE])
pg.display.set_caption("Tilfeldige figurer")

klokke = pg.time.Clock()
FPS = 2

farger = ["yellow", "red", "blue", "green", "magenta"]

def sirkel(min_r, maks_r):
    r = randint(min_r, maks_r)
    x = randint(r, BREDDE//2 - r)
    y = randint(r, HOYDE//2 - r)
    pg.draw.circle(vindu, choice(farger), (x, y), r)

def kvadrat(min_s, maks_s):
    s = randint(min_s, maks_s)
    x = randint(BREDDE//2, BREDDE - s)
    y = randint(0, HOYDE//2 - s)
    pg.draw.rect(vindu, choice(farger), (x, y, s, s))

def rektangel(min_s, maks_s):
    b = randint(min_s, maks_s)
    h = randint(min_s, maks_s)
    x = randint(0, BREDDE//2 - b)
    y = randint(HOYDE//2, HOYDE - h)
    pg.draw.rect(vindu, choice(farger), (x, y, b, h))

def ellipse(min_s, maks_s):
    b = randint(min_s, maks_s)
    h = randint(min_s, maks_s)
    x = randint(BREDDE//2, BREDDE - b)
    y = randint(HOYDE//2, HOYDE - h)
    pg.draw.ellipse(vindu, choice(farger), (x, y, b, h))

fortsett = True


while fortsett:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill("black")
    min = 20
    maks = 50

    # Streker
    pg.draw.line(vindu, "white", (BREDDE/2, 0), (BREDDE/2, HOYDE), 2)
    pg.draw.line(vindu, "white", (0, HOYDE/2), (BREDDE, HOYDE/2), 2)
    for _ in range(10):
        sirkel(min, maks)
        kvadrat(min, maks)
        rektangel(min, maks)
        ellipse(min, maks)

    pg.display.update()
    klokke.tick(FPS)

pg.quit()