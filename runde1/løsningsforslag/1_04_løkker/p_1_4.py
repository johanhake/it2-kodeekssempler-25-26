print('\n1.4.1') 
for i in range(1,4):
    print('i: '+ str(i))
    for j in range(1,3):
        print('i: '+ str(i) +' og j: ' + str(j)) 

print('\n1.4.2') 
for i in range(100,79,-2):
    print(str(i)+' ', end='')

print('\n\n1.4.3')
for i in range(1,11):
    print(f'{i**3:6}',end='' )
# eller en liste
print('\n',[x**3 for x in range(1,11)])

#print('\n1.4.4\n  |',end='')
print('\n  |',end='')
for i in range (1,6): print(f'{i:4}',end='')
print('\n' + '-'*23, end='')
for rad in range(1,6):
    print('\n' + str(rad) + ' |', end='')
    for kolonne in range(1,6):
        print(f'{rad*kolonne:4}',end='')

print('\n\n1.4.5')
tab = [0,1]
f2  = 0
f1  = 1
f   = f2 + f1

while f <= 1000:
    tab.append(f)
    f2 = f1
    f1 = f
    f  = f2 + f1

print('Fibonaccitallene under 1000:', end='')
i = 0
for f in tab:  
    if i%5==0:
        print() # ny rad
    i += 1
    print(f'{f: 5}', end='')

# Smidig IT-2 © TIP AS 2024