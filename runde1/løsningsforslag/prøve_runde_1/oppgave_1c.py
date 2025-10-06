while True:
    try:
        høyde = int(input("Angi høyde i cm: "))
    except:
        print("Feil! Skriv inn et heltall for høyde!")
        continue
    try: 
        vekt = int(input("Angi vekt i kg: "))
        break
    except:
        print("Feil! Skriv inn et heltall for høyde!")
        
print("BMI:", round(vekt/(høyde/100)**2, 1))

