# Går ikke igjennom denne.

# FEIL
tall = [1,2,3,3,3,4,3,3,3,5,3,3,6,3]
for t in tall:
    if t == 3:
        tall.remove(t)
print(tall)

# index out of range
tall = [1,2,3,3,3,4,3,3,3,5,3,3,6,3]
for i in range(len(tall)):
    if tall[i] == 3:
        tall.pop(i)
print(tall)

# RIKTIG
tall = [1,2,3,3,3,4,3,3,3,5,3,3,6,3]
for i in range(len(tall)-1,-1,-1):
    if tall[i] == 3:
        tall.pop(i)
print(tall)

tall = [1,2,3,3,3,4,3,3,3,5,3,3,6,3]
tall = [x for x in tall if x != 3]
print(tall)

tall = [1,2,3,3,3,4,3,3,3,5,3,3,6,3]
while 3 in tall:
    tall.remove(3)
print(tall)
