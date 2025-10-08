personer = [
    {'navn':'Knut' ,'alder':32},
    {'navn':'Tiril','alder':28},
    {'navn':'Anne' ,'alder':41},
    {'navn':'Oscar','alder':35}
]

#a = personer[2]
#print(a["navn"], a["alder"])

# Nøkkel funksjon som henter ut verdien til alder fra et element. 
def key_alder(a):
    return a["alder"]

for a in sorted(personer, key=key_alder, reverse=True):
    print(a['navn'], a['alder'])
    #print(*a.values())
