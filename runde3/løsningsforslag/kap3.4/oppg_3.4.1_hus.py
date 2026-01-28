# Oppgave 3.4.1 Tegn et hus
import pygame as pg
from pygame.locals import *

pg.init()

BREDDE, HØYDE = 600, 500

vindu = pg.display.set_mode([BREDDE, HØYDE])
pg.display.set_caption("Hus")

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill("darkblue") # Bakgrunn/himmel
    
    # Tegn et hus
    pg.draw.rect(vindu, 'darkgreen', (0,350,600,150)) # Gress
    pg.draw.rect(vindu, 'red3', (100,200,300,200)) # Hus
    pg.draw.rect(vindu, 'orange', (150,250,50,50)) # Vindu med lys
    pg.draw.rect(vindu, 'black', (150,250,50,50),2) # Vindusramme
    pg.draw.line(vindu, 'black', (175,250),(175,300),2) # Sprosse
    pg.draw.line(vindu, 'black', (150,275),(200,275),2) # Sprosse
    pg.draw.rect(vindu, 'black', (300,250,50,50)) # Mørkt vindu
    pg.draw.rect(vindu, 'chocolate4', (225,300,50,100)) # Dør
    pg.draw.polygon(vindu, 'black', ((75,200),(250,100),(425,200))) # Tak
    pg.draw.rect(vindu, 'black', (300,100,50,100)) # Pipe
    pg.draw.circle(vindu, 'grey', (500,100), 40) # Måne

    pg.display.update()

pg.quit()