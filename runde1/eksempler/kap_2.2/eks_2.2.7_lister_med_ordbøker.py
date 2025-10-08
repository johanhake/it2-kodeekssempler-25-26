personer = [
    {'navn':'Knut' ,'alder':32},
    {'navn':'Tiril','alder':28},
    {'navn':'Anne' ,'alder':41},
    {'navn':'Oscar','alder':35}
]

#a = personer[2]
#print(a["navn"], a["alder"])

def key_alder(a):
    return a["alder"]

for a in sorted(personer, key=key_alder, reverse=True):
    print(a['navn'], a['alder'])
