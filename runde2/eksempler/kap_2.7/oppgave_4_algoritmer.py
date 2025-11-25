# SET n TO 10 
# SET a[0] TO 0 
# SET a[1] TO 1 
# FOR hvert heltall i fra og med 2 til n 
#   SET a[i] TO a[i-1] + a[i-2] 
# ENDFOR 
# DISPLAY a[n]

n = 10
a = [0, 1]
for i in range(2,n):
    a.append(a[i-1]+a[i-2])
print(a[n])

partall = 0
a = [0, 1]
i = 2
while partall < 10:
    tall = a[i-1]+a[i-2]
    if tall % 2 == 0:
        print(tall)
        partall += 1
    a.append(tall)
    i += 1