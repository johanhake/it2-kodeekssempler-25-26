# 1.6.1 b
with open('heltall.txt') as fil:
    lines = fil.readlines()
    print(f'Filen inneholder {len(lines)} tall.')
    print(f'Summen av tallene er {sum(int(line) for line in lines)}.')
    print('Tallene er ', end='')
    for line in lines: print(f'{int(line):5}', end='')

# Smidig IT-2 © TIP AS 2024