import pygame as pg

pg.init()
BREDDE = 500
HØYDE  = 500

vindu = pg.display.set_mode([BREDDE, HØYDE])
font = pg.font.SysFont("Arial", 34)

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill("black")
    pg.draw.circle(vindu, "red", (100, 250), 50)
    pg.draw.circle(vindu, 'purple', (250, 200), 50,10)

    pg.draw.rect(vindu, "blue", (200, 250, 90, 90))
    pg.draw.rect(vindu, 'green', (50, 300, 100, 50),10)

    pg.draw.arc(vindu, 'orange', (50, 50, 250, 100), 0, 1.5*3.14, 5)

    pg.draw.line(vindu, (205, 0, 205), (400, 100), (420, 400), 5)

    pg.draw.ellipse(vindu, (255, 192, 203), (50, 350, 250, 100))

    bilde = font.render("Heisann!", True, (255, 255, 255))
    vindu.blit(bilde, (250, 20))

    pg.display.flip()

pg.quit()
