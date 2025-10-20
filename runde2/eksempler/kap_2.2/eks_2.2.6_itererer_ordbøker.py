ordbok = {
    'fornavn':'Per',
    'yrke':'Snekker',
    'fødselsår':1992,
    'poststed':'Askim'
}

print(list(ordbok.keys()))

print()
# Iterasjon over nøkler:
for key in ordbok.keys():
    print(key)

print()
for verdi in ordbok.values():
    print(verdi)
    
print()
for key, verdi in ordbok.items():
    print(f"{key} -> {verdi}")
    