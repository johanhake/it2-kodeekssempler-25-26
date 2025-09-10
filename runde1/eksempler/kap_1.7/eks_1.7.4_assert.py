def aldersgruppe(alder):
    if alder < 18:
        return 'barn'
    elif alder < 68:
        return 'voksen'
    else:
        return 'pensjonist'

assert aldersgruppe(10) == 'barn'
assert aldersgruppe(17) == 'barn'
assert aldersgruppe(18) == 'voksen'
assert aldersgruppe(60) == 'voksen'
assert aldersgruppe(67) == 'voksen'
assert aldersgruppe(68) == 'pensjonist'
print("Alt gikk fint!")
