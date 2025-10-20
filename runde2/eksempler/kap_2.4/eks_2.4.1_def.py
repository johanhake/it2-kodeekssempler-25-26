def f(x):
    return x**2

def jada():
    print("JADA")
    
def bada(a=1, b=0, c=0):
    return a*"JADA"+b*"BADA"+c*"SNADA"


print(f(2)+2*f(3))
print(jada())
print(bada(2, 5))
print(bada(b=3,a=2))