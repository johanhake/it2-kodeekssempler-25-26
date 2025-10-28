from planet import Planet
        
jupiter = Planet("Jupiter", 778.5, 69911, 4)
jupiter.vis_info()
print(f"Volumet til {jupiter.navn} er {jupiter.volum():.2e}")
    
