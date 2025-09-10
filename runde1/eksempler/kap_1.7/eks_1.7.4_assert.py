def aldersgruppe(alder):
    if alder < 18:
        return 'barn'
    else:
        return 'voksen'

assert aldersgruppe(10)=='barn'
