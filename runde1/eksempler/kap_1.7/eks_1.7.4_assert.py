def aldersgruppe(alder):
    if alder < 18:
        return 'barn'
    else:
        return 'voksen'

assert aldersgruppe(10)=='barn'
assert aldersgruppe(17)=='barn'
assert aldersgruppe(18)=='voksen'
assert aldersgruppe(50)=='voksen'
assert aldersgruppe(66)=='voksen'
assert aldersgruppe(67)=='pensjonist'
assert aldersgruppe(80)=='pensjonist'