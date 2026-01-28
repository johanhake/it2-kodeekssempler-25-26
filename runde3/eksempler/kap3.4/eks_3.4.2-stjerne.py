import pygame as pg
import math as m

pg.init()
BREDDE = 500
HØYDE  = 500

vindu = pg.display.set_mode((BREDDE, HØYDE))
font = pg.font.SysFont("Arial", 34)


def star_points(cx, cy, R, start_angle=-m.pi/2, clockwise=True):
    """
    Generer 10 polygonpunkter for en regulær femkantet stjerne (pentagram).
    
    Parametre:
        cx, cy      : senterkoordinater
        R           : ytterradius (fra senter til spiss)
        start_angle : startvinkel (rad). -pi/2 gir en spiss rett opp.
        clockwise   : True for klokkeretning, False for mot-klokkeretning
    
    Returnerer:
        Liste av (x, y) med 10 punkter som danner stjernepolygonet.
    """
    # Inneradius for regulær femstjerne
    r = R * (m.sin(m.pi/10) / m.sin(3*m.pi/10))  # ≈ 0.381966 * R
    
    # Vinkel mellom påfølgende punkter (ytter/inner/ytter/...)
    step = m.pi / 5  # 36 grader
    
    # Retningsfaktor
    dir_ = -1 if clockwise else 1
    
    pts = []
    for i in range(10):
        # Partallsindeks -> ytterpunkt, oddetall -> innerpunkt
        radius = R if i % 2 == 0 else r
        angle = start_angle + dir_ * i * step
        x = cx + radius * m.cos(angle)
        y = cy + radius * m.sin(angle)
        pts.append((x, y))
    return pts

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    vindu.fill("black")

    pg.draw.circle(vindu, "white", (200, 200), 200)
    pg.draw.polygon(vindu, "red", star_points(200, 200, 200))
    pg.display.update()

pg.quit()
