a = float(input("Skriv inn a: "))
toleranse = float(input("Skriv inn en presisjon: "))

x_neste = a/2
x = a
n = 0
while abs(x-x_neste) > toleranse:
    x = x_neste
    x_neste = (x + a/x)/2
    n += 1
print(f"Kvadratroten til {a} er {x_neste}. Det tok {n} iterasjoner.")

