antall_kolonner = 15
teller = 0

for tall in range(1, 101, 2):
    teller += 1
    print(f'{tall:4}', end='')
    if teller % antall_kolonner == 0:
        print()