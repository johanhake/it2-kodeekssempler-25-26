# Gitt listen tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Skriv et program som fjerner annet hvert element fra listen
# slik at den blir [10, 30, 50, 70, 90].
tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tall)
i = 1
while i < len(tall):
    del tall[i]
    i += 1
print(tall)

tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tall)
for i in range(len(tall)-1,-1,-2):
    del tall[i]
print(tall)

tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tall)
tall = [tall[i] for i in range(0,len(tall),2)]
print(tall)

tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tall)
tall = [x for x in tall if x % 20 != 0]
print(tall)

tall = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(tall)
tall = tall[::2]
print(tall)

# Smidig IT-2 © TIP AS 2024