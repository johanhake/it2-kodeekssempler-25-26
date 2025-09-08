print('Når du er ferdig med å skrive inn tall,')
print('kan du trykke Enter uten å skrive noe.')

# Du skrev inn 45
# Du skrev inn 23
# jada er ikke et heltall.
# Du skrev inn 67
# Vi slutter!
# Du skrev inn følgende tall: [45, 23, 67]

tall = []
while True:
    tekst_inn = input('Skriv inn et helttall: ')
    tall.append(int(tekst_inn))
    print(f'Du skrev inn {tekst_inn}')
    if tekst_inn == '':
        print("Vi slutter!")
        break

print("Du skrev inn følgende tall:", tall)
