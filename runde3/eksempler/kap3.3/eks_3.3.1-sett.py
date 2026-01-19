# Fjerner duplikater
sett_1 = {1,2,3,3,2,1}     
print(type(sett_1),sett_1)
liste = [1,2,3,3,2,1]
print(type(liste),liste)

# Fjerner duplikater i en listen
sett_2 = set(liste)        
print(type(sett_2),sett_2)

# Konverterer tilbake til liste
liste2 = list(sett_2)
print(type(liste2),liste2)

