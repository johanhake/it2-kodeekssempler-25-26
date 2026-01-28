import pygame as pg

# Initialiserer/starter pygame
pg.init()

BREDDE = 500
HØYDE  = 500
vindu = pg.display.set_mode([BREDDE, HØYDE])
pg.display.set_caption("Flagg")


def sveriges_flagg(x, y, bredde):
    høyde = bredde*(5/8)
    blå = (0, 106, 167)
    gul = (254, 204, 0)
    pg.draw.rect(vindu, blå, (x, y, bredde, høyde))
    pg.draw.rect(vindu, gul, (x, y+høyde*2/5, bredde, høyde/5))
    pg.draw.rect(vindu, gul, (x+5/16*bredde, y, bredde/8, høyde))

fortsett = True
while fortsett:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill("black")
    sveriges_flagg(50, 50, 150)
    sveriges_flagg(250, 50, 50)
    sveriges_flagg(50, 250, 250)

    pg.display.flip()

pg.quit()