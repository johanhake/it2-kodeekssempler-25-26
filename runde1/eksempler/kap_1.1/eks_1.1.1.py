# Verdier leses inn fra brukeren inn og vises til brukeren
navn = input("Hva heter du? ")
print("Hallo, " + navn + "!")

# Verdier behandles og lagres
a = 1 + 2
b = a + 3
          
a = 4    
print(a)
print(b)

# If-setning brukes til å utføre kode på grunnlag av verdien til en betingelse
alder = 10       
if alder < 16:
    pris = 15
else:
    pris = 25

print(pris)

# Løkker brukes til å gjenta kode
liste = [3,8,5,11,7]
verdi = 0
for tall in liste:
    verdi = verdi + tall
print(liste)
print(verdi)

# Funksjoner brukes til å lagre kode til bruk seinere
def finn_maks(liste):
    maks = liste[0]                          
    for tall in liste:
        if tall > maks:
            maks = tall
    return maks

liste1 = [3,8,5,11,7]
print(liste1)
print(finn_maks(liste1))