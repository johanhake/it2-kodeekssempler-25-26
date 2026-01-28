import pygame as pg

pg.init()
BREDDE = 500
HØYDE  = 500

vindu = pg.display.set_mode((BREDDE, HØYDE))
vindu.fill("black")

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

        # Check for mouse events
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     print(f"Mouse button pressed at {event.pos}, button: {event.button}")
        #     pg.draw.circle(vindu, "red", event.pos, 10)
        
        # if event.type == pg.MOUSEBUTTONUP:
        #     print(f"Mouse button released at {event.pos}, button: {event.button}")
            
        if event.type == pg.MOUSEMOTION:
            # event.pos gives absolute position (x, y)
            # event.rel gives relative movement (rel_x, rel_y)
            # event.buttons is a tuple of boolean states for (left, middle, right) buttons
            pass # Use this for tracking mouse movement
            print(f"Mouse move event {event.pos}, button: {event.buttons}")
            if event.buttons[0]:
                pg.draw.circle(vindu, "red", event.pos, 10)
            

    pg.display.update()

pg.quit()

