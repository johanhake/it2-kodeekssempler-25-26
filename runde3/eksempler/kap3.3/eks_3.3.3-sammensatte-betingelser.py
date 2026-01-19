høyde = 181
blå_øyne = False
vekt = 74

if høyde > 180 and blå_øyne and vekt < 75:
    print("3 krav OK")
else:
    print("3 krav IKKE OK")

if høyde > 180 or blå_øyne or vekt < 75:
    print("minst 1 krav OK")
else:
    print("minst 1 krav IKKE OK")

if sum((høyde > 180, blå_øyne, vekt < 75)) >= 2:
    print("minst 2 krav OK")
else:
    print("minst 2 krav IKKE OK")
