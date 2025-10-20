import math


# Definer en funksjon som returnerer et desimaltall
def f(x: float) -> float:
    return x**2 - 4*x + 3


print('f(x)=x^2-4x+3')
for x in range(6):
    print(f'f({x}) = {f(x)}')
print()


# Definer en funksjon som returnerer en tuppel
def kvadrat_og_kubikk(x: float) -> tuple[float, float]:
    return x**2, math.pow(x, 3)


print('x, x^2 og x^3')
for x in 1, 3, 6:
    x_2, x_3 = kvadrat_og_kubikk(x)
    print(f'x = {x:2}, x^2 = {x_2:2} og x^3 = {x_3:5}')
print()


# Definer en funksjonen som returnerer en ordbok (dict)
def hent_sirkel_info(radius: float) -> dict:
    omkrets = 2*math.pi*radius
    areal = math.pi*radius**2
    return {'radius': radius, 'omkrets': omkrets, 'areal': areal}


for radius in 3, 4:
    print('\nSirkelinfo for radius', radius)
    for nøkkel, verdi in hent_sirkel_info(radius).items():
        print(f'{nøkkel.title():8}: {verdi:5.2f}')
