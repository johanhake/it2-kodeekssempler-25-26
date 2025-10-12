def eksempel_1():
    lokal_var = "Jeg er lokal."
    print(f'Inni funksjonen, lokal_var: {lokal_var}')
    print(f'Inni funksjonen, global_var: {global_var}')


print("Eksempel 1")
global_var = "Jeg er global."
print(f'Utenfor, før funksjonskallet: {global_var}')
eksempel_1()
print(local_var)


def eksempel_2():
    global_var = "Jeg er nå lokal."
    print(f'Inni funksjonen: {global_var}')


print("\nEksempel 2:")
global_var = "Jeg er global."
print(f'Utenfor, før funksjonskallet: {global_var}')
eksempel_2()
print(f'Utenfor, etter funksjonskallet: {global_var}')


def eksempel_3():
    global global_var
    global_var = "Jeg har blitt endret."
    print(f"Inni funksjonen,: {global_var} ID: {id(global_var)}")


print("\nEksempel 3:")
global_var = "Jeg er global."
print(f'Utenfor, før funksjonskallet: {global_var} ID: {id(global_var)}')
eksempel_3()
print(f'Utenfor, etter funksjonskallet: {global_var} ID: {id(global_var)}')


def eksempel_4():
    global_var = "Jeg er nå lokal."
    print(f"Inni funksjonen, global_var: {global_var} ID: {id(global_var)}")
    globals()["global_var"] = "Jeg har blitt endret."
    tekst = 'Inni funksjonen,  globals()["global_var"]:'
    print(
        f'{tekst} {globals()["global_var"]} ID: {id(globals()["global_var"])}')


print("\nEksempel 4:")
global_var = "Jeg er global."
print(f'Utenfor, før funksjonskallet: {global_var} ID: {id(global_var)}')
eksempel_4()
print(f'Utenfor, etter funksjonskallet: {global_var} ID: {id(global_var)}')

print("\nEksempel Rabatt:")
rabatt_grense = 1000
rabatt_prosent = 20


def rabatt(pris: float) -> float:
    if pris > rabatt_grense:
        rabatt = (pris-rabatt_grense)*rabatt_prosent/100
    else:
        rabatt = 0
    return rabatt


pris = 2499
print(f'Pris: {pris:7.2f}, rabatt: {rabatt(pris):7.2f}')
rabatt_grense = 2000
print(f'Pris: {pris:7.2f}, rabatt: {rabatt(pris):7.2f}')

# Smidig IT-2 © TIP AS, 2024