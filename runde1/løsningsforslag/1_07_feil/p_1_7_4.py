print('\n\n1.7.4')
tab = [0, 1]
f2, f1 = 0, 1
f = f2 + f1

while f <= 1000:
    tab.append(f)
    f2, f1 = f1, f
    f = f2 + f1

print('Fibonaccitallene under 1000:', end='')
i = 0
for f in tab:
    if i % 5 == 0:
        print()  # ny rad
    i += 1
    print(f'{f: 5}', end='')

# Smidig IT-2 © TIP AS 2024