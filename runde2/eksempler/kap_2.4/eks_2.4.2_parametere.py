def skriv_ut_fag(*fag):
    print(type(fag))
    print(len(fag))
    if not fag:
        print('Jeg liker ingen fag.')
    else:
        tekst = ', '.join(fag)
        før, _, etter = tekst.rpartition(', ')
        print(f'Jeg liker {før} og {etter}.')


print()
skriv_ut_fag()
skriv_ut_fag('engelsk', 'tysk')
skriv_ut_fag('it', 'biologi', 'psykologi')

def skriv_ut_personalia(**personalia):
    print(type(personalia))
    print(len(personalia))
    if not personalia:
        print('Ingen opplysnger.')
    else:
        for nøkkel, verdi in personalia.items():
            print(f'{nøkkel.title():10}: {str(verdi).title()}')
    print()

skriv_ut_personalia()
skriv_ut_personalia(navn='joakim jensen', bosted='jessheim')
skriv_ut_personalia(navn='karl kruse', født=1993, yrke='konsulent')