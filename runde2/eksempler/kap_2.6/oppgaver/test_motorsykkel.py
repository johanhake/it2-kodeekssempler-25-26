from motorsykkel import Motorsykkel

def hovedprogram():
    m1 = Motorsykkel("BMW", "DN8932")
    m2 = Motorsykkel("Honda", "DN8933")
    m3 = Motorsykkel("Kawasaki", "DN8934")

    m1.skriv_ut()
    m2.skriv_ut()
    m3.skriv_ut()

    m3.kjor(10)
    print(m3.hent_kilometerstand())

hovedprogram()